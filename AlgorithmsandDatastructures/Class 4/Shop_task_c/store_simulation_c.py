import json
import random
import time
from collections import deque
from multiprocessing import Process, JoinableQueue, current_process, cpu_count

# Load products and customers from JSON
with open('products.json', 'r') as f:
    products = json.load(f)

with open('customers.json', 'r') as f:
    customers = json.load(f)


# Define Cashier Process
class Cashier:
    def __init__(self, name):
        self.name = name

    def process_customer(self, customer, discounts):
        total_price = sum([product['price'] for product in customer['products']])
        discount_amount = sum([self.apply_discount(product, discounts) for product in customer['products']])
        discounted_price = total_price - discount_amount
        if customer['has_loyalty_card']:
            discounted_price *= 0.9  # 10% loyalty card discount
        return total_price, discounted_price

    def apply_discount(self, product, discounts):
        for discount in discounts:
            if discount['type'] == 'category' and discount['value'] == product['category']:
                return product['price'] * discount['discount']
            elif discount['type'] == 'product' and discount['value'] == product['name']:
                return product['price'] * discount['discount']
        return 0


def cashier_process(customer_queue, discounts, report_queue, cashier_id):
    cashier = Cashier(name=f"Cashier_{cashier_id}")
    count = 0
    while True:
        customer = customer_queue.get()
        if customer is None:  # Stop signal
            customer_queue.task_done()
            break
        total_price, discounted_price = cashier.process_customer(customer, discounts)
        customer_report = {
            'customer_id': customer['id'],
            'customer_name': customer['name'],
            'products': [{'id': product['id'], 'name': product['name'], 'price': product['price']} for product in
                         customer['products']],
            'total_price_without_discount': round(total_price, 2),
            'total_amount_spent_with_discount': round(discounted_price, 2),
            'cashier_name': cashier.name
        }
        report_queue.put(customer_report)
        customer_queue.task_done()
        count += 1
        if count >= 50:
            time.sleep(1)  # Cashier takes a short break
            count = 0


# Discounts
discounts = [
    {'type': 'category', 'value': 'tyres', 'discount': 0.1},
    {'type': 'product', 'value': 'frames_product_1', 'discount': 0.2},
    # Add more discounts as needed
]


def customer_shopping(customer_queue, customers, shopping_time=0.5):
    for customer in customers:
        customer_queue.put(customer)
        time.sleep(random.uniform(0.05, shopping_time))  # Simulate shopping time
    for _ in range(cpu_count()):  # Send stop signal to cashiers
        customer_queue.put(None)


if __name__ == '__main__':
    customer_queue = JoinableQueue()
    report_queue = JoinableQueue()
    customer_process = Process(target=customer_shopping, args=(customer_queue, customers))
    cashiers = [Process(target=cashier_process, args=(customer_queue, discounts, report_queue, i + 1)) for i in
                range(cpu_count())]

    customer_process.start()
    for cashier in cashiers:
        cashier.start()

    customer_process.join()
    customer_queue.join()

    daily_report = []
    while not report_queue.empty():
        daily_report.append(report_queue.get())

    # Save daily report to JSON
    with open('daily_report.json', 'w') as f:
        json.dump(daily_report, f, indent=4)

    print("Simulation completed. Report generated.")
