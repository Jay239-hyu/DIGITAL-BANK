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
            self.history.append(f"Deposited: {amount}")
            print(f"Deposit amount is {amount}, new balance is {self.__balance}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        MAX_WITHDRAW = 25000
        if amount > self.__balance:
            print("No sufficient funds, sorry!")
        elif amount < 0:
            print("Amount must be positive!")
        elif(amount>0 and amount<=MAX_WITHDRAW):
            self.__balance -= amount
            self.history.append(f"Withdraw: {amount}")
            print(f"Withdraw amount {amount}, new balance is {self.__balance}")
        elif amount > MAX_WITHDRAW:
            self.__balance -= MAX_WITHDRAW
            self.history.append(f"withdraw: {MAX_WITHDRAW}")
            print(f"Withdraw amount 25000 , new balance is {self.__balance}")
            print(f"Sorry but you reached the withdrawal limit. withdraw remaining amount {amount - MAX_WITHDRAW} in your next transection.. ")
    
    def transection(self, receiver , amount):
        if amount <= 0:
         print("Amount must be positive!")
         return

        if self.__balance >= amount:
            self.__balance -= amount
            receiver.__balance += amount
            print(f"{amount} transferred from {self.acc_no} to {receiver.acc_no}")
        else:
            print("Insufficient funds!")
        
        self.__history.append(f"Send:{amount} to {receiver.__acc_no}")
        receiver.__history.append(f"Receive:{amount} from {self.__acc_no}")
    
    
    def check_balance(self):
        print(f"{self.__name}'s account balance = {self.__balance}")


    def show_history(self):
        print("Transaction History:")
        for entry in self.history: 
            print(entry)

    def load_history(self, history_list):
        self.__history = history_list



        

