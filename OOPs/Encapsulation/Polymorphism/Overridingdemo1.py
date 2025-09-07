class Parent:
    def home(self):
        print("Parent function is called")
class Child(Parent):
    def home(self):
        # print("Child function is called")
        return super().home()   #with help of super we can call parent function 
c=Child()
c.home()    #if we create child object and we return function with super then parent function will be called 
# else simple c.home will call child function