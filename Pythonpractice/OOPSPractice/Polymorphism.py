#operator overloading

# class Distance():
#     def __init__(self,kms):
#         self.kms=kms
#     def __add__(self,other):

#         return self.kms+other.kms
#     def __gt__(self,other):

#         return self.kms>other.kms
#     def __lt__(self,other):

#         return self.kms<other.kms
# D=Distance(50)
# D1=Distance(70)
# d2=D+D1
# print(d2)
# d3=D>D1
# print(d3)
# d4=D<D1
# print(d4)


#Overriding 

class Animal():
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
        # super().sound()
class cat(Animal):
    def sound(self):
        print("Cat meow meow")
        # super().sound()
A=Animal()
A.sound()

d=Dog()
d.sound()

c=cat()
c.sound()