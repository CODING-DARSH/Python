# no1=int(input("Enter no1:"))
# no2=int(input("Enter no2:"))
# try:
#     x=no1/no2
#     print(x)
# except:
#     print("Cannot divide by zero")
#it should show us error even if we give it as string but for that error it should give enter valid digit not this error that says can't divide by zero

# try:
#     no1=int(input("Enter no1:"))
#     no2=int(input("Enter no2:"))
#     x=no1/no2
#     print(x)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Enter digits only")


# we can also create object for this error and we can display that error

# try:
#     no1=int(input("Enter no1:"))
#     no2=int(input("Enter no2:"))
#     x=no1/no2
#     print(x)
# except ZeroDivisionError as e:
#     # print("Cannot divide by zero")
#     print(e)
# except ValueError as e:
#     # print("Enter digits only")
#     print(e)

# there is also a block named finally which we works like it will execute for sure whether it is try or exceptional block


# try:
#     no1=int(input("Enter no1:"))
#     no2=int(input("Enter no2:"))
#     x=no1/no2
#     print(x)
# except ZeroDivisionError as e:
#     # print("Cannot divide by zero")
#     print(e)
# except ValueError as e:
#     # print("Enter digits only")
#     print(e)
# finally:
#     print("Finally block is executed")


no1=int(input("Enter no1:"))
no2=int(input("Enter no2:"))
x=no1/no2
print(x)

