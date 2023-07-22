# Multiple Inheritance

class Phone:
    #constructor
    def __init__(self,brand,price):
        self.price = price
        self.brand = brand

    def buy(self):
        print(f"You bought a {self.brand} phone..!!")

class Smartphone:
    #constructor
    def __init__(self,brand,price,os,ram):
        self.price = price
        self.brand = brand
        self.os = os
        self.ram = ram

    def buy(self):
        print(f"You bought {self.brand} smartphone...!!")


#Multiple inheritance
class FuturisticPhone(Smartphone,Phone):
    pass



fp1 = FuturisticPhone("Samsung",100000,"Android", "8GB")
fp1.buy()