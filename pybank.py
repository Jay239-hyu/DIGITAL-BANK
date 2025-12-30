from Account import Account
from BankData import BankData
from utils import hash_pin
import getpass


def main():
    while True:
        # Main program
        print("Welcome to the Python Bank!")
        print("1. Register")
        print("2. Login")


        choice = input("Enter your choice:  ")
        if choice == "1":
            name = input("Set your username to create account:  ")
            pin = getpass.getpass("Enter your 4 digit PIN :  ")
            status , account_number = BankData.create_account(name , pin)

            if status == "INVALID PIN":
                print("Invalid PIN")
            elif status == "SUCCESS":
                print(f"Account was created in our DataBase and your account number is {account_number}")

        elif choice == "2":
            acc_no = input("Enter account number: ")
            count = 1   
            while count <= 3:
                pin = getpass.getpass("Enter PIN: ")
                hashed_input = hash_pin(pin)
                status , acc  = BankData.load_account(acc_no, hashed_input)

                
                if status == "SUCCESS":
                    print("✅ Login success")
                    break  #--> Break the login loop

                elif(status == "WRONG_PIN"):
                    print(f"Incorrect PIN , Your remaining tries for login:{3-count}")
                    count += 1
                    continue

                elif(status == "NO_ACCOUNT"):
                    print("Account doesn't exist in our Database")
                    break  #--> Break the login loop
                
                    
            if status == "SUCCESS":

                while True: 
                    print("\nChoose an option:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transaction")
                    print("4. Check Balance")
                    print("5. Show History")
                    print("6. Exit")

                    option = input("Enter the number number after checked the Menu:  ")
                    
                    if option == '1':
                        amount = int(input("Enter the amount to deposit:  "))
                        status , msg  = acc.deposit(amount)
                        if status == "SUCCESS":
                            BankData.save_account(acc.acc_no , acc)
                            print(msg)
                        if status == "NEGATIVE AMOUNT":
                            print(msg)
                        if status == "INVALID":
                            print(msg)

                    elif option == '2':
                        amount = int(input("Enter the amount to withdrawal:  "))
                        status , msg = acc.withdraw(amount)
                        if status == "SUCCESS":
                            BankData.save_account(acc.acc_no , acc)
                            print(msg)
                        if status == "NEGATIVE AMOUNT":
                            print(msg)
                        if status == "NO FUNDS":
                            print(msg)
                        if status == "INVALID":
                            print(msg)

                    elif option == '3':
                        receiver_acc_no = int(input("Enter the receiver's account number:  "))
                        amount = int(input("Enter the amount to transfar:  "))
                        status , receiver = BankData.load_account_by_acc_no(receiver_acc_no)
                        if status == 'SUCCESS':
                            status , msg = acc.transection(receiver , amount)
                            if status == "NEGATIVE AMOUNT":
                                print(msg)
                            elif status == "NO FUNDS":
                                print(msg)
                            elif status == "INVALID":
                                print(msg)
                            elif status == "SUCCESS":
                                BankData.save_account(acc.acc_no , acc)
                                BankData.save_account(receiver.acc_no , receiver)
                                print(msg)
                        else:
                            print("Can't find receiver's account in our DataBase.")
                        
                    elif option == '4':
                        msg = acc.check_balance()
                        print(msg)

                    elif option == '5':
                       for h in acc.show_history():
                           print(h)

                    else:
                        print("Logged out successfully.")
                        break   # breaks account menu loop

                        
if __name__ == "__main__":
    main()


                

               
            
        
  
            






          

        


        


