class Bank:
    def __init__(self,nameOfBank):  #self is must declared permanent, nameofBank="ICICI"
        self.nameofBank=nameOfBank  #it works like self.nameOfBank="ICICI"
    def UserDetails(self):
        print("Users bank is ",self.nameofBank)
b1=Bank("ICICI")    #Means for b1 object if constructor is called then self.nameOfBank="ICICI" and after that with b1 object if function is called then that assign value of that variable for that object will be passed or given 
b1.UserDetails()
b2=Bank("SBI")
b2.UserDetails()
        