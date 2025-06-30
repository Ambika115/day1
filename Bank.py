class bannk:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
b=Bank()
b.deposit(1000)
b.deposit(1200)
print(b.get_balance())