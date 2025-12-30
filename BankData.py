import os , json , getpass 
from utils import hash_pin
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
        if account_number not in accounts:
            return ("NO_ACCOUNT" , None)

        data = accounts[account_number]
        acc = Account(account_number, data["name"], data["pin"], data["balance"]) #Here acc is a object of Account class.
        acc.load_history(data.get("history" , []))
        return ("SUCCESS",acc)
    
    @staticmethod
    def load_account(account_number, hashed_input):
        if account_number not in accounts:
            return ("NO_ACCOUNT" , None)
        
        if accounts[account_number]["pin"] != hashed_input:
            return ("WRONG_PIN" , None)
        
        data = accounts[account_number]
        acc = Account(account_number, data["name"], data["pin"], data["balance"])
        acc.load_history(data.get("history" , []))
        return ("SUCCESS" , acc)
     
    @staticmethod
    def create_account(name , pin):
            if len(pin) != 4 or not pin.isdigit():
                return("INVALID PIN",None)
        
            hashed_pin = hash_pin(pin)
            account_number = str(len(accounts) + 1001)
            new_account = Account(account_number, name, hashed_pin) #Here New account is a object of Bankaccount class.
            BankData.save_account(account_number, new_account)
            return ("SUCCESS" , account_number)

      
        






