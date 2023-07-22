class Bank:

    #class variables
    __min_balance = 10000

    def __init__(self):
        self.balance = 0
        self.__intRate = 10   # private variable declared
        print("in the __init__")
    def get_intRate(self):
        return self.__intRate
    def set_intRate(self,variable):
        self.__intRate = variable

    @classmethod
    def set_min_balance(cls, min_balance):
        cls.__min_balance = min_balance

    @staticmethod
    def get_tax(balance):
        tax = 20
        return (tax/100)*balance

customer1 = Bank();
print(customer1.balance)
# print(customer1.__intRate) ------ Not accessable private variables outside scope
print(customer1._Bank__intRate)
print(customer1.get_intRate) 

#modifying class method
customer1.set_min_balance = 5000
print(customer1._Bank__min_balance)