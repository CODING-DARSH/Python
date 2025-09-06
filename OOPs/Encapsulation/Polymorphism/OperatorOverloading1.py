class Student:
    def __init__(self,*marks):  #default constructor with args is passed
        self.marks=marks
    def __add__(self,other):
        print("self..",self.marks)
        print("other..",other.marks)
        return self.marks+other.marks
amit=Student(10)
sumit=Student(20)
# amit=Student(10,20,30)
# sumit=Student(10,20,30)
total=amit+sumit
print(total)

#args will return tuple which are mutable