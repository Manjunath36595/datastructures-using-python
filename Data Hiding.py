class AccountHolder:
    def __init__(self):
        self.AccountNumber = 12345678
        self.__balance = 3456
        self.__password = 123

    def setPassword(self, p):
        self.__password = p

    def getPassword(self):
        return self.__password

a = AccountHolder()

print(a.AccountNumber)
print(a._AccountHolder__balance)
print(a.getPassword())

"""
OUTPUT:

12345678
3456
123



"""
