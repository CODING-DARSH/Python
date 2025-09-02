name  = input("enter name :")
upperName = ""

for i in name:
    if ord(i)>=97 and ord(i)<=122:
        upperName = upperName + chr(ord(i)-32)
    else:
        
        #upperName =  upperName + chr(ord(i))    
        upperName = upperName +i

print(upperName)        
        