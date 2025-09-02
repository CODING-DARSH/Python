# def getData(**kwargs):
#     print(kwargs) #dict

# getData(name="ram",age=22,salary=20000,city="Ahmedabad")  
  
# def getData(**kwargs):
#     print(kwargs) #dict

#getData(name="ram",age=22,salary=20000,city="Ahmedabad",100)   error 


# def getData(**kwargs,x): #error
#     print(kwargs) #dict

# getData(name="ram",age=22,salary=20000,city="Ahmedabad")  

def getData(x,**kwargs): #error
    print(kwargs) #dict

#getData(100,name="ram",age=22,salary=20000,city="Ahmedabad")  
getData(x = 100,name="ram",age=22,salary=20000,city="Ahmedabad")  