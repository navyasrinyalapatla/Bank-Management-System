import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="bank_db"
)

cursor = connection.cursor()

customer_name = input("Enter Customer Name: ")
mobile = input("Enter Mobile Number: ")
aadhar = input("Enter Aadhar Number: ")
account_type = input("Enter Account Type: ")
balance = float(input("Enter Initial Balance: "))

cursor.execute(
    """
    INSERT INTO customers
    (customer_name, mobile, aadhar, account_type, balance)
    VALUES (%s, %s, %s, %s, %s)
    """,
    (customer_name, mobile, aadhar, account_type, balance)
)

connection.commit()

print("Customer Added Successfully!")