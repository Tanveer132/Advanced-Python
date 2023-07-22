# create stack and its functionality methods
class stack:
    def __init__(self):
        self.array=[]
    def add(self, variable):
        self.array.append(variable)
    def remove(self,variable):
        self.array.pop()


# test stack objects
stack1 = stack()
print(stack1.array)

stack1.add(10)
stack1.add(20)
stack1.add(30)
print(stack1.array)

stack1.remove(20)
print(stack1.array)