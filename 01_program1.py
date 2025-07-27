import json
import os
import hashlib
import sys
import getpass

ACCOUNT_FILE = "accounts.json"


if os.path.exists(ACCOUNT_FILE):
    with open(ACCOUNT_FILE, "r") as f:  
        accounts = json.load(f)
else:
    accounts = {} 

class BankAccount:
    def __init__(self,acc_no, name, pin, balance=0):
        self.acc_no = acc_no
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
        elif(amount>0 and amount<=25000):
            self.balance -= amount
            self.history.append(f"Withdrew: {amount}")
            print(f"Withdrew amount {amount}, new balance is {self.balance}")
        elif amount > 25000:
            self.balance -= 25000
            self.history.append("withdraw: 25000")
            print(f"Withdrew amount 25000 , new balance is {self.balance}")
            print(f"Sorry but you reached the withdrawal limit. withdraw remaining amount {amount - 25000} in your next transection.. ")

    def transection(self, receiver , amount):

        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            print(f"{amount} transferred from {self.acc_no} to {receiver.acc_no}")
        else:
            print("Insufficient funds!")
        
        self.history.append(f"Send:{amount} to {receiver.acc_no}")
        receiver.history.append(f"Receive:{amount} from {self.acc_no}")

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

def load_account_by_acc_no(account_number):
    if account_number in accounts:
        data = accounts[account_number]
        acc = BankAccount(account_number, data["name"], data["pin"], data["balance"]) #Here acc is a object of BankAccount class.

        acc.history = data.get("history", [])
        return acc
    else: 
     return None
    

def load_account(account_number, hashed_input):
    if account_number in accounts and accounts[account_number]["pin"] == hashed_input:
        data = accounts[account_number]
        acc = BankAccount(account_number, data["name"], data["pin"], data["balance"])
        acc.history = data.get("history", [])
        return acc
    else:
     return None
    
while True:
    # Main program
    print("Welcome to the Python Bank!")
    print("1. Register")
    print("2. Login")
    choice = input("Choose option: ")
    
    if choice == "1":
        name = input("Enter your name: ")
        while True:
          pin = getpass.getpass("Set 4-digit PIN: ")
          if len(pin) != 4 or not pin.isdigit():
            print("❌ Invalid PIN. Please enter exactly 4 numeric digits.")
            continue
          break
    
        hashed_pin = hash_pin(pin)
        account_number = str(len(accounts) + 1001)
        new_account = BankAccount(account_number, name, hashed_pin) #Here New account is a object of Bankaccount class.
        save_account(account_number, new_account)
        print(f"Account created! Your account number is: {account_number}")
       

    elif choice == "2":
        
        acc_no = input("Enter account number: ")
        if acc_no not in accounts:
             print("❌ Account not found. Please register first.")
             continue

        count = 1   
        while count <= 3:
         pin = getpass.getpass("Enter PIN: ")
         hashed_input = hash_pin(pin)
         account = load_account(acc_no, hashed_input)
       
    
            
            
         if account:
            print("✅ Login success")



                
            while True: 
                print("\\nChoose an option:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transection")
                print("4. Check Balance")
                print("5. Show History")
                print("6. Exit")

                choice = input("Enter choice (1/2/3/4/5): ")

                if choice == "1":
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == "2":
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)

                elif choice == "3":
                    receivers_acc_number = input("Enter receiver's account number:  ")
                    amount = int(input("Enter the transection amount:  "))
                    input_pin = hash_pin(getpass.getpass("Please Renter your 4-Digit pin for just security purpose:  "))
                    if accounts[acc_no]['pin'] == input_pin:
                        receiver = load_account_by_acc_no(receivers_acc_number)
                        account.transection(receiver , amount)
                    else:
                        print("Enter the right pin please....!")
                    save_account(account.acc_no, account)
                    save_account(receiver.acc_no, receiver)

                elif choice == "4":
                    account.check_balance()
                elif choice == "5":
                    account.show_history()
                elif choice == "6":
                    save_account(acc_no, account)
                    print("Logged out successfully.")
                    sys.exit()
                    
                else:
                    print("Invalid choice. Please try again.")
        
         else:              
            print("❌ Login failed")
            print(f"Please enter the valid pin! now you have only {3-count} attempts") 
            count += 1





                
     
            
        
  
            






          

        


        


