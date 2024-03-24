"""
Create a class called "BankAccount" with attributes for account number and balance.
Add methods to the BankAccount class for depositing and withdrawing money.
Create a subclass of BankAccount called "SavingsAccount" with an additional attribute for interest rate.
Override the BankAccount class's withdraw method in the SavingsAccount subclass to include a fee for each withdrawal.
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")


# In this code, the BankAccount class is defined with an __init__ method that initializes the account_number and
# balance attributes. The deposit method allows you to add money to the account by increasing the balance attribute.
# The 'withdraw' method allows you to withdraw money from the account by decreasing the balance attribute, but
# it checks if the amount is greater than the available balance before performing the withdrawal.

# To create a subclass called "SavingsAccount" with an additional attribute for interest rate, you can
# define the subclass as follows:

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        fee = 0.05 * amount  # Calculate the fee as 5% of the withdrawal amount
        if amount + fee <= self.balance:
            self.balance -= amount + fee
        else:
            print("Insufficient funds")


# In this code, the SavingsAccount class is defined as a subclass of BankAccount. It inherits the account_number and
# balance attributes from the BankAccount class. The __init__ method is overridden to include the additional
# interest_rate attribute. The withdraw method is also overridden to include a fee for each withdrawal.
# The fee is calculated as 5% of the withdrawal amount and deducted from the balance along with the withdrawal amount.
#
# Now you can create instances of the BankAccount and SavingsAccount classes and use their methods to deposit and
# withdraw money:

# Create a BankAccount instance
bank_account = BankAccount("123456789", 1000)

# Deposit money
bank_account.deposit(500)

# Withdraw money
bank_account.withdraw(200)

# Create a SavingsAccount instance
savings_account = SavingsAccount("987654321", 2000, 0.02)

# Deposit money
savings_account.deposit(1000)

# Withdraw money (including fee)
savings_account.withdraw(500)
