import json
from collections import deque

with open('products.json', 'r') as f:
    products = json.load(f)

with open('customers.json', 'r') as f:
    customers = json.load(f)


class Cashier:
    def __init__(self, name):
        self.name = name

    def process_customer(self, customer, discounts):
        total_price = sum([product['price'] for product in customer['products']])
        discount_amount = sum([self.apply_discount(product, discounts) for product in customer['products']])
        discounted_price = total_price - discount_amount
        if customer['has_loyalty_card']:
            discounted_price *= 0.9
        return total_price, discounted_price

    def apply_discount(self, product, discounts):
        for discount in discounts:
            if discount['type'] == 'category' and discount['value'] == product['category']:
                return product['price'] * discount['discount']
            elif discount['type'] == 'product' and discount['value'] == product['name']:
                return product['price'] * discount['discount']
        return 0


discounts = [
    {'type': 'category', 'value': 'tyres', 'discount': 0.1},
    {'type': 'product', 'value': 'frames_product_1', 'discount': 0.2},
    # Add more discounts as needed
]

queue = deque(customers)

cashier = Cashier(name="John Doe")
daily_report = []

while queue:
    customer = queue.popleft()
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
    daily_report.append(customer_report)

with open('daily_report.json', 'w') as f:
    json.dump(daily_report, f, indent=4)

print("Simulation completed. Report generated.")
