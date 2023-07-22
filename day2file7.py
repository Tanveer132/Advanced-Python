#Special methods

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} has price {self.price}"
    
    def __add__(self,other):
        return self.price + other.price

p1 = Product("Iphone", 20000)
p2 = Product("Iphone", 20000)
print(p1)
print(p1+p2)