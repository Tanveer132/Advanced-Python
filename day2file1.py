#Aggregation

class Customer:
    def __init__(self,name,age,address,email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def print_details(self):
        print(
            f"{self.name} lives in {self.address.area} has Email Id - {self.email.username}")

class Address:
    def __init__(self,door,street,area,pincode):
        self.door = door
        self.street = street
        self.area = area
        self.pincode = pincode

class Email:
    def __init__(self,username,hostname):
        self.username = username
        self.hostname = hostname


address1 = Address(20, "Any street", "Any area", 415506)
email1 = Email("tanveer.shikalgar","infosys.com")

customer1 = Customer("Tanveer", 24, address1, email1)

customer1.print_details()
