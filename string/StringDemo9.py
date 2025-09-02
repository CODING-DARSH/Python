name = "java"
char = "x"
index = -1

for i in range(0,len(name)):
    #j == a FALSE i =0
    #a ==a True  i =1
    if name[i]==char:
        index = i #index = 1
        break
   

print("index = ",index) 
        

