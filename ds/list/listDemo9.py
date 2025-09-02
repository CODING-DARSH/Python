scores = [["virat",100,71,91],["rohit",90,80,20],["ms",20,111,90]]
#ouput: [["virat",total],["rohit",total],["ms",total]]

# x  =[] #
# x.append([10,20])
# print(x)

x =[]
name =""
sum=0
for i in range(0,len(scores)):
    #print(scores[i])
    name = scores[i][0]
    #print(name)
    for j in range(1,len(scores[i])):
        # print(scores[i][j])
        sum = sum + scores[i][j]
    
    x.append([name,sum])    
    sum=0
print(x)    
        