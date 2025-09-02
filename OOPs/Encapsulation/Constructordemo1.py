class Bank:
    def __init__(self): #__init__ is widely used for declaring constructor
        self.name="ICICI"   #it is hardcoded or predeclared name of bank
    def getUserDetails(self):
        print("User has bank account in ",self.name)
b1=Bank()
b1.getUserDetails()
b2=Bank()
b2.getUserDetails()