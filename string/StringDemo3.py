#reverse string
name = "naman" #4 0 1 2 3 
revName = ""

#print(name[4])
for i in range(len(name)-1,-1,-1):
    #print(name[i])
    revName = revName + name[i] #revName = ""+a = a
                                #a = "a"+v = "av"
                                #av = av+a = ava
                                #ava = ava+j = avaj

print(f"revname = {revName}")                                
 
 
if name == revName:
     print("name is palindrome ")
else:
    print("name is not palindrome")     