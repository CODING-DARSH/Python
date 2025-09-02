def demo():
    print("demo function called...")
    print("this is demo function.....")
    
    #without return type without argument...



demo() #calling part...    


#with argument without return...
def add(a,b):
    print(f"value of a = {a}")
    print(f"value of b = {b}")

add(10,20)    
add("a","b")
add([],())    




def average(a,b,c):
    print("average function called...")
    return (a + b+ c)/3


ans = average(10,20,30)
print(f"ans = {ans}")
print("ans = ",average(100,200,300))
print(f" ans = {average(1000,2000,3000)}")



#boolean...
def isActive():
    return False

if isActive():
    print("if....")
else:
    print("else....")    
