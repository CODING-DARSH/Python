users = ("amit","sumit")

#users[0]="AMIT"

userList = list(users)
userList.append("raj")
users = tuple(userList)
print(users)


a = (1,2,3)
b = (4,5,6)
c = a + b
print(c)