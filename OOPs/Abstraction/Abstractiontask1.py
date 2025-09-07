from abc import ABC,abstractmethod
class OLA(ABC):
    @abstractmethod     #As we have given @abstractmethod in parent class this means that it is compulsory to add this function in all child class
    def CalculateFare(self):
        pass
#once u give this as abstraction u cant create object for this

class Car(OLA):
    def __init__(self,km):      #we have declared constructor here                      
        self.km=km
        self.rate=15
    def CalculateFare(self):
        price=self.rate*self.km
        print(f"Price of fare for car is...{price}")
class Bike(OLA):
    def __init__(self,km):
        self.km=km
        self.rate=10
    def CalculateFare(self):
        price=self.rate*self.km
        print(f"Price of fare for bike is...{price}")
class Ricks(OLA):
    def __init__(self,km):
        self.km=km
        self.rate=12
    def CalculateFare(self):
        km=30
        price=self.rate*self.km
        print(f"Price of fare of Ricks is...{price}")
c=Car(10)
c.CalculateFare()

B=Bike(25)
B.CalculateFare()

R=Ricks(20)
R.CalculateFare()