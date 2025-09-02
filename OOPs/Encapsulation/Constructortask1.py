class Bank:
    def __init__(self,name,age,*deposit):
        self.name=name
        self.age=age
        self.balance=sum(deposit)
    def display(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.balance}")
b1=Bank("Darsh",18,1000,2000,3000)
b1.display()