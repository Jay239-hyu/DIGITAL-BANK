import json
import os
import hashlib

ACCOUNT_FILE = "accounts.json"


if os.path.exists(ACCOUNT_FILE):
    with open(ACCOUNT_FILE, "r") as f:
        accounts = json.load(f)
else:
    accounts = {}

class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []
       
   

       

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: {amount}")
            print(f"Deposit amount is {amount}, new balance is {self.balance}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("No sufficient funds, sorry!")
        elif amount < 0:
            print("Amount must be positive!")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew: {amount}")
            print(f"Withdrew amount {amount}, new balance is {self.balance}")

    def check_balance(self):
        print(f"{self.name}'s account balance = {self.balance}")

    def show_history(self):
        print("Transaction History:")
        for entry in self.history:
            print(entry)


def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()


def save_account(account_number, account):
    accounts[account_number] = {
        "name": account.name,
        "pin": account.pin,
        "balance": account.balance,
        "history": account.history
        
    }
    with open(ACCOUNT_FILE, "w") as f:
        json.dump(accounts, f , indent=4)

def load_account(account_number, pin):
    if account_number in accounts and accounts[account_number]["pin"] == hashed_input:
        data = accounts[account_number]
        acc = BankAccount(data["name"], data["pin"], data["balance"])
        acc.history = data.get("history", [])
        return acc
    else:
        print("Invalid account number or PIN.")
        return None
while True:
    # Main program
    print("Welcome to the Python Bank!")
    print("1. Register")
    print("2. Login")
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter your name: ")
        pin = input("Set a 4-digit PIN: ")
        hashed_pin = hash_pin(pin)
        account_number = str(len(accounts) + 1001)
        new_account = BankAccount(name, hashed_pin)
        save_account(account_number, new_account)
        print(f"Account created! Your account number is: {account_number}")

    elif choice == "2":
        acc_no = input("Enter account number: ")
        pin = input("Enter PIN: ")
        hashed_input = hash_pin(pin)
        account = load_account(acc_no, hashed_input)
    
    


        if accounts[acc_no]["pin"] == hashed_input:
        

            while True:
                print("\\nChoose an option:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Show History")
                print("5. Exit")

                choice = input("Enter choice (1/2/3/4/5): ")

                if choice == "1":
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == "2":
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == "3":
                    account.check_balance()
                elif choice == "4":
                    account.show_history()
                elif choice == "5":
                    save_account(acc_no, account)
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please try again.")



