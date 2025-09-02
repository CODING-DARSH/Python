class Car:
    def __init__(self):
        print("Parent constructor is called")
        self.type="sedan"
        self.seat=5
    def engine(self):
        print("engine")
class BMW(Car):
    def __init__(self):
        print("Child class default constructor is callled")
        super().__init__()
    def getDetails(self):
        self.engine()
        print(f"{self.seat}")
        print(f"{self.type}")
c1=BMW()
c1.getDetails()