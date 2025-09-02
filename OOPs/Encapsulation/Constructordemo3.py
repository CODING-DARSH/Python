class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def studentDetails(self):
        print("Name of student is ",self.name)
        print("Age of student is ",self.age)
s1=student("Darsh",18)
s1.studentDetails()
s2=student("Aryaa",19)
s2.studentDetails()