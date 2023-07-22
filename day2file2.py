#Association

class Customer:
    def __init__(self,name,cust_type,bill):
        self.name=name
        self.cust_type=cust_type
        self.bill=bill
    
    def calculate_bill(self):
        tax1=Tax(self.cust_type)
        final_bill = self.bill - tax1.tax_details()
        print(final_bill)
    
class Tax:
    def __init__(self,cust_type):
        self.cust_type=cust_type
    
    def tax_details(self):
        if (self.cust_type == "Normal"):
            return 20
        else:
            return 10
cust1=Customer("Rock","Normal",100)
cust1.calculate_bill()
