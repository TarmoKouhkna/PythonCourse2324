class BankAccount:
    def __init__(self, balance=0, account_number=None):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"Account Number: {self.account_number}\nBalance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, interest_rate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest. New balance: {self.balance}")


class PayPalAccount(BankAccount):
    def __init__(self, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email

    def send_money(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Sent {amount} to {recipient}. New balance: {self.balance}")
        else:
            print("Insufficient funds")


class UnderThePillowAccount(BankAccount):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def hide_money(self, amount):
        self.balance -= amount
        print(f"Hid {amount} under the pillow. New balance: {self.balance}")


# Example usage:
savings_acc = SavingsAccount(interest_rate=0.05, balance=1000, account_number="SAV123")
paypal_acc = PayPalAccount(email="example@example.com", balance=500, account_number="PAY456")
pillow_acc = UnderThePillowAccount(balance=200, account_number="PIL789")

print("Savings Account:")
print(savings_acc)
savings_acc.deposit(500)
savings_acc.add_interest()
print(savings_acc)

print("\nPayPal Account:")
print(paypal_acc)
paypal_acc.send_money("friend@example.com", 200)
print(paypal_acc)

print("\nUnder The Pillow Account:")
print(pillow_acc)
pillow_acc.hide_money(50)
print(pillow_acc)
