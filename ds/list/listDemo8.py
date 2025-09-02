data = [[10,20,30],[10,30,30],[10,20,20]]
#data =[60,70,50]


x =[]
sum =0
for i in data:
    for j in i:
        #print(j)
        sum = sum + j
    x.append(sum)    
    sum=0

print(x)    
        
        