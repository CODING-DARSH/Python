# def getStudents(name):
#     print(name)

# getStudents("raj")    
# getStudents("raj","jay","parth")



#args -- arguments *it is not a keyword
def getStudents(*args):
    print(args)
    

getStudents("ram")
getStudents("ram","shyam")    
getStudents("ram","shyam","amit","summit")
getStudents()


def getEmployees(y,*args,x):
    print(args)        
    print(x)
    print(y)


#getEmployees("ram","rahul","raj","ok")  #error
getEmployees("ram","rahul","raj",x="ok")      