from abc import ABC,abstractmethod
class UPI:
    @abstractmethod
    def transfer(self):
        # print("Transfer function of upi class is called")
        pass
class SBI(UPI):
    @abstractmethod
    def transfer(self):
        print("Transfer function of SBI is called")
s=SBI()
s.transfer()