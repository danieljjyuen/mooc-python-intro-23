# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name:str, number:str, balance:float):
        self.__name = name
        self.__number = number
        self.__balance = balance
    
    # @property
    # def name(self):
    #     return self.__name

    # @name.setter
    # def name(self, name):
    #     self.__name = name
    
    # @property
    # def number(self):
    #     return self.__number
    
    # @number.setter
    # def number(self, number):
    #     self.__number = number
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance
    
    def deposit(self, amount:float):
        self.balance+=amount
        self.__service_charge()

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance-= amount
            self.__service_charge()
    
    def __service_charge(self):
        self.balance*=.99

# account = BankAccount("Randy Riches", "12345-6789", 1000)
# account.withdraw(100)
# print(account.balance)
# account.deposit(100)
# print(account.balance)



