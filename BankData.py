import os , json
from Account import Account

ACCOUNT_FILE = "accounts.json"

if os.path.exists(ACCOUNT_FILE):
    try:
        with open(ACCOUNT_FILE, "r") as f:
            accounts = json.load(f)  #--> Here we converted whole JSON data to Python Dict.
    except json.JSONDecodeError: 
        print("Warning: accounts.json is corrupted. Starting with empty database.")
        accounts = {}
else:
    accounts = {}


class BankData:

    @staticmethod
    def save_account(account_number, account):
        accounts[account_number] = {
            "name": account.name,
            "pin": account.pin,
            "balance": account.balance,
            "history": account.history
        }
            
        with open(ACCOUNT_FILE, "w") as f:
            json.dump(accounts, f , indent=4)
    
    @staticmethod
    def load_account_by_acc_no(account_number):
        if account_number in accounts:
            data = accounts[account_number]
            acc = Account(account_number, data["name"], data["pin"], data["balance"]) #Here acc is a object of Account class.
            acc.load_history(data.get("history" , []))
            return acc
        else: 
            print("Sorry, can't find your account in our database please ensure that your bank account was created in our Bank. Thank You! ")
      
    
    @staticmethod
    def load_account(account_number, hashed_input):
        if account_number in accounts and accounts[account_number]["pin"] == hashed_input:
            data = accounts[account_number]
            acc = Account(account_number, data["name"], data["pin"], data["balance"])
            acc.load_history(data.get("history" , []))
            return acc
        else:
            print("Sorry, can't find This account in our database please ensure that this account is exitsted in out bank or not, Thank You!")
      
        






