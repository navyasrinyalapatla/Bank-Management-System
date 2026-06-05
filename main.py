import mysql.connector
from bank_account import BankAccount

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="bank_db"
)

cursor = connection.cursor()

customer_name = input("Enter Customer Name: ")

cursor.execute(
    "SELECT customer_name, balance FROM customers WHERE customer_name = %s",
    (customer_name,)
)

row = cursor.fetchone()
if row is None:
    print("Customer not found!")
    exit()

account = BankAccount(row[0], float(row[1]))
print("\n1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. View All Customers")

choice = input("Choose an option (1,2,3 or 4): ")

if choice == "1":
    amount = float(input("Enter Amount: "))
    account.deposit(amount)

elif choice == "2":
    amount = float(input("Enter Amount: "))
    account.withdraw(amount)
    
elif choice == "3":
    account.show_balance()
elif choice == "4":
    cursor.execute("SELECT customer_name, balance FROM customers")

    for customer in cursor:
        print(customer)

cursor.execute(
    "UPDATE customers SET balance = %s WHERE customer_name = %s",
    (account.balance, account.customer_name)
)

connection.commit()

