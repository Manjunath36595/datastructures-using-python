class AccountHolder:
    def __init__(self):
        self.accountNumber = 12345678
        self.__balance = 3456
        self.__password = 123
    def set_password(self, p):
        self.__password = p
    def get_password(self):
        return self.__password
a = AccountHolder()
print(a._AccountHolder__balance)


"""
OUTPUT:

3456



"""
