#ano.... no named function...
#function as object..

def test():
    print("test function called...")
    return 100


#print(test())
print(test)
# x = test()
# print(x)

x = test #adderess copy x
print(x)
#test == x
x()
