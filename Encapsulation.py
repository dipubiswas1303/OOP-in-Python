class Atm:
    
    #Constructor
    
    def __init__(self):
        
        self.__pin = ""    #making variable private __vName
        self.__balance = 0 #to access it ddirectly use _className__vName
                           #nothing in python is truly private
        self.menu()

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("pin changed")
        else:
            print("Not Allow")
            

    def menu(self):
        
        user_input = input("""
                    Hello, How would you like to proceed?
                           1. Enter 1 to create pin.
                           2. Enter 2 to deposit.
                           3. Enter 3 to withdraw
                           4. Enter 4 to cheak balance
                           5. Enter 5 to Exit
                    """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print('bye')
        
    def create_pin(self):
        self.__pin = input("Enter your pin:")
        print("pin set completed")

    def deposit(self):
        temp = input("Enter your pin:")
        if temp == self.__pin:
            amount = int(input("Enter the amount:"))
            self.__balance = self.__balance + amount
            print("Deposited")
        else:
            print("Invalid pin")
    
    def withdraw(self):
        temp = input('Enter your pin:')
        if temp == self.__pin:
            amount = int(input('Enter the amount:'))
            if amount < self.__balance:
                self.__balance = self.__balance -amount
                print('Done')
            else:
                print("Insuficient Balance")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input('Enter your pin: ')
        if temp == self.__pin:
            print(self.__balance)
        else:
            print('Invaild pin')