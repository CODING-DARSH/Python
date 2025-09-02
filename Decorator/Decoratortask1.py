# getAccess(role,name)
# 	print(name is accessing this function having "role".)

def user(func):#it will go here (2)
    def inner(role,name):#data given in getAccess will come here
        if role=="admin":
            print("U can access the name and data")#if admin is role then
            func("admin","Darsh")#it will call this and value given here will be passed or given to getAccess
        else:
            print("Sorry u cant access the name")
    return inner

@user
def getAccess(role,name):
    print(f"{name} is accessing the function having {role}")
getAccess("admin","darsh")#this will execute first(1)