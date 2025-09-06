# create a multipule same name funciton is same class called funciton overloading
from multipledispatch import dispatch
class Shape:
    @dispatch()
    def area(self):
        print("Python function is called without parameters")
    @dispatch(float)
    def area(self,r):
        print("Python function for area of circle is callled with 1 parameter",r)
    @dispatch(int,int)
    def area(self,h,w):
        print("Python function for area of circle is callled with 2 parameter",h,w)
s=Shape()
s.area()
s.area(3.9)
s.area(2,3)