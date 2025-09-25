class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def displayvehicle(self):   
        print(f"Brand of vehicle {self.brand}")
        print(f"Year of manufacturing of vehicle {self.year}")
class Car(Vehicle):
    def __init__(self,brand,year,seat):
        self.seat=seat
        super().__init__(brand,year)
    def displayCar(self):
        print(f"Car has {self.seat} seats")
class ElectricCar(Car):
    def __init__(self,brand,year,seat,battery_capacity):
        self.battery_capacity=battery_capacity
        super().__init__(brand,year,seat)
    def displayElectricCar(self):
        print(f" Battery capacity of car is {self.battery_capacity}")
Ec=ElectricCar("BMW",2025,5,12000)
Ec.displayvehicle()
Ec.displayCar()
Ec.displayElectricCar() #