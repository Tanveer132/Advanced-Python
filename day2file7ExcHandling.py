#Customers can have many credit cards which they can use for purchasing. Each credit card has number and balance.
#purchase_item() method takes price and item. validates if price is less than credit balance. 
class InvalidCardNumException(Exception):
    def __init__(self):
        super().__init__("Invalid card Selected.")

class LowBalanceException(Exception):
    def __init__(self):
        super().__init__("Insufficient balance.")

class creditCard:
    def __init__(self,cardNumber, balance):
        self.cardNumber = cardNumber
        self.balance = balance

class Customer:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def purchase_item(self, price, cardNumber):
        print("In purchase")
        if price<0:
            print("price validation failed")
            raise Exception()
        if cardNumber not in self.cards:
            print("cardNumber validation failed")
            raise InvalidCardNumException()
        if self.cards[cardNumber].balance <price:
            print("balance validation failed")
            raise LowBalanceException()
        

    def __str__(self):
        return f" {self.name} has cards" 
        
crd1 = creditCard(101, 1000)
crd2 = creditCard(102,2000)
crd3 = creditCard(103,1500)
cards = {crd1.cardNumber:crd1, crd2.cardNumber:crd2, crd3.cardNumber:crd3}

customer1 = Customer("Tanveer",cards)
print(customer1)
customer1.purchase_item(5000, 1001)
# customer1.purchase_item(5000, 101)