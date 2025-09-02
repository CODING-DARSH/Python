#lambda params : body

# def test():
#     print("test called..")

x = lambda :print("test called")
x()

# def test(a,b):
#     print(f"add  = {a+b}")

# test(100,20)    

# x1 = lambda a,b : print(f"add = {a+b}")
# x1(100,200)

# def add(a,b,c):
#     return a+b+c

# ans = add(10,20,30)
# print(f"ans = {ans}")

#no return keyword
x2 = lambda a,b,c : a+b+c
ans = x2(10,20,30)
print(f"ans = {ans}")
print(f"ans = {x2(1,2,3)}")


x3 = lambda fname,lname : fname+"-"+lname
print(x3("ram","sharma"))
