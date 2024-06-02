import random
import json
from collections import namedtuple, deque, defaultdict
from decimal import Decimal


categories = ['tyres', 'wheels', 'frames', 'handlebars', 'stems', 'saddle posts', 'saddles', 'groupsets', 'pedals']
products = []

Product = namedtuple('Product', ['name', 'price', 'category'])

for category in categories:
    for i in range(50):
        product = Product(name=f"{category}_product_{i}", price=round(random.uniform(10, 200), 2), category=category)
        products.append(product)

with open('products.json', 'w') as f:
    json.dump([product._asdict() for product in products], f, indent=4)

Customer = namedtuple('Customer', ['name', 'products', 'has_loyalty_card'])

customers = []

for i in range(150):
    customer_name = f"Customer_{i}"
    has_loyalty_card = random.choice([True, False])
    customer_products = random.sample(products, random.randint(1, 10))
    customer = Customer(name=customer_name, products=customer_products, has_loyalty_card=has_loyalty_card)
    customers.append(customer)


class Cashier:
    def __init__(self, name):
        self.name = name

    def process_customer(self, customer, discounts):
        total_price = sum([product.price for product in customer.products])
        discount_amount = sum([self.apply_discount(product, discounts) for product in customer.products])
        discounted_price = total_price - discount_amount
        if customer.has_loyalty_card:
            discounted_price *= 0.9  # 10% loyalty card discount
        return total_price, discounted_price

    def apply_discount(self, product, discounts):
        for discount in discounts:
            if discount['type'] == 'category' and discount['value'] == product.category:
                return product.price * discount['discount']
            elif discount['type'] == 'product' and discount['value'] == product.name:
                return product.price * discount['discount']
        return 0


queue = deque(customers)

# Step 5: Discounts
discounts = [
    {'type': 'category', 'value': 'tyres', 'discount': 0.1},
    {'type': 'product', 'value': 'frames_product_1', 'discount': 0.2},
    # Add more discounts as needed
]

cashier = Cashier(name="John Doe")
daily_report = []

while queue:
    customer = queue.popleft()
    total_price, discounted_price = cashier.process_customer(customer, discounts)
    customer_report = {
        'customer_name': customer.name,
        'products': [{'name': product.name, 'price': product.price} for product in customer.products],
        'total_price_without_discount': round(total_price, 2),
        'total_amount_spent_with_discount': round(discounted_price, 2),
        'cashier_name': cashier.name
    }
    daily_report.append(customer_report)

with open('daily_report.json', 'w') as f:
    json.dump(daily_report, f, indent=4)

print("Simulation completed. Report generated.")
