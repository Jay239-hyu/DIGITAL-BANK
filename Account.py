class Account:
    def __init__(self , acc_no , name , pin , balance = 0):
        self.__acc_no = acc_no
        self.__name = name
        self.__pin = pin
        self.__balance = balance
        self.__history = []
    
       
    @property
    def balance(self):
        return self.__balance
    
    @property
    def acc_no(self):
        return self.__acc_no
    
    @property
    def name(self):
        return self.__name
    
    @property
    def pin(self):
        return self.__pin
    
    @property
    def history(self):
        return self.__history.copy()
    

    def deposit(self, amount): 
        if amount > 0:
            self.__balance += amount
            self.__history.append(f"Deposited: {amount}")
            return("SUCCESS",f"Deposit amount is {amount}, new balance is {self.__balance}")
        elif(amount < 0):
            return("NEGATIVE AMOUNT" , "Amount should be in positive")
        else:
            return("INVALID" , "Please Enter a valid number")
        
        

    def withdraw(self, amount):
        MAX_WITHDRAW = 25000
        if amount > self.__balance:
            return("NO FUNDS","No sufficient funds, sorry!")
        elif amount < 0:
            return("NEGATIVE AMOUNT","Amount must be positive!")
        elif(amount>0 and amount<=MAX_WITHDRAW):
            self.__balance -= amount
            self.__history.append(f"Withdraw: {amount}")
            return("SUCCESS",f"Withdraw amount {amount}, new balance is {self.__balance}")
        elif amount > MAX_WITHDRAW:
            self.__balance -= MAX_WITHDRAW
            self.__history.append(f"withdraw: {MAX_WITHDRAW}")
            return("SUCCESS", f"Withdraw amount {MAX_WITHDRAW} , new balance is {self.__balance}")
        else:
            return("INVALID" , "Please Enter a valid number")

    def transection(self, receiver , amount):
        if amount <= 0:
            return("NEGATIVE AMOUNT" , "Amount must be positive!")
         
        if self.__balance >= amount:
            self.__balance -= amount
            receiver.__balance += amount

            self.__history.append(f"Send:{amount} to {receiver.__acc_no}")
            receiver.__history.append(f"Receive:{amount} from {self.__acc_no}")

            return("SUCCESS",f"{amount} transferred from {self.acc_no} to {receiver.acc_no}")
        
        elif(amount > self.__balance):
            return("NO FUNDS","Insufficient funds!")
        else:
            return("INVALID" , "Please Enter a valid number")
        
        
    
    def check_balance(self):
        return(f"{self.__name}'s account balance = {self.__balance}")

    def show_history(self):
        return self.__history

    def load_history(self, history_list):
        self.__history = history_list



        

