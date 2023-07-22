# Multilevel Inheritance

class Phone:
    #constructor
    def __init__(self,brand,price):
        self.price = price
        self.brand = brand

    def buy(self):
        print(f"You bought a {self.brand} phone..!!")

class Smartphone(Phone):
    #constructor
    def __init__(self,brand,price,os,ram):
        super().__init__(brand,10000)
        self.os = os
        self.ram = ram

    def buy(self):
        print(f"You bought {self.brand} smartphone...!!")


#Multilevel inheritance
class FuturisticPhone(Smartphone):
    def buy(self):
        print(f"You bought Futuristic phone")
        super().buy()


sm1 = Smartphone("Samsung",100000,"Android", "8GB")
sm1.buy()

fp1 = FuturisticPhone("Samsung",100000,"Android", "8GB")
fp1.buy()