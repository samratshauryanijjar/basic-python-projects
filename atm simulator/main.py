# ATM Machine Simulator
import os
print("Welcome to Python Bank")

with open('balance.txt','r')as f:
       balance = int(f.read()) 
def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if username == "admin" and password == "1234":
        print("Login Successful!")
        return True

    elif username == "admin" and password != "1234":
        print("Invalid password.")
        return False

    elif username != "admin" and password == "1234":
        print("Invalid username.")
        return False

    else:
        print("Login credentials are invalid.")
        return False


if login():

    while True:

        print("\n====== PYTHON BANK ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Your balance is: $", balance)

        elif choice == "2":
            amount = int(input("How much do you want to deposit? "))

            balance += amount
            with open("balance.txt", "w") as f:
                f.write(str(balance))

            print("$", amount, "deposited successfully.")
            print("Your new balance is: $", balance)

        elif choice == "3":
            amount = int(input("How much do you want to withdraw? "))

            if amount <= balance:
                balance -= amount
                with open("balance.txt", "w") as f:
                    f.write(str(balance))
                print("$", amount, "withdrawn successfully.")
                print("Your new balance is: $", balance)
            else:
                print("Insufficient balance.")

        elif choice == "4":
            print("Thanks for choosing Python Bank!")
            break

        else:
            print("Invalid option. Please try again.")