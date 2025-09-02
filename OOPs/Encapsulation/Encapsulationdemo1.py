class Demo:
    x=1000  #it is global variable which is declared inside class and can be accessed anytime using object

    def test(self): #self is declared as parameter but it is actually equal to object which is created
                    #for example d is object then self==d
        a=100   #it is a local variable  it can use only in scope
        self.b=100  #it is instance variable
        #it will create no of object copy
        #it can be use with same object within class
        print("Test function inside Demo class is called")
    def display(self):
        print("Value of  a=",self.b)
        print("Value of  x=",self.x)
d=Demo()
d.test()    #it is actually as d.test(d) if we don't write self in function it will show error
d.display()