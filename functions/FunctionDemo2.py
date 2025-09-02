def getUserData(name,salary,age,city):
    print(f"name = {name}")
    print(f"salary = {salary}")
    print(f"age = {age}")
    print(f"city = {city}")


#getUserData("ram",20000,20)    
#getUserData(20,"ram",20000)
#named param

#getUserData(name = "ram",age=22,salary=32000,)    
#getUserData(name = "ram",age=22,salary=32000,"ahmedabad")#error     
getUserData("ram",age=22,salary=32000,city="ahmedabad")    
    