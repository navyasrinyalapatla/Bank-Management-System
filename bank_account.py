class BankAccount:

    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.balance = balance

    def show_balance(self):
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited:", amount)
        else:
            print("Invalid Amount")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")
        