class Student:
    def __init__(self,*marks):
        self.marks=marks
    def __eq__(self, other):
        return self.marks==other.marks

s1=Student(10,20,30)
s2=Student(10,20,31)

if s1==s2:
    print("Both students have same marks")
else:
    print("Both student dosen't have same marks")
