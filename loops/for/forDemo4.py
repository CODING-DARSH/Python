#fibbonacci series
#no1 = 0
#no2 = 1

#0 1 1 2 3 5 8

no1 = 0
no2 = 1
print(f"{no1} {no2}",end=" ") #0 1
sum=0
for i in range(1,10):
    sum = no1 + no2 # 0 +1 = 1 # 1+1 =2 #1+2=3 #2+3 =5,#3+5=8
    print(f"{sum}",end= " ") # 1 2 3 5 8
    no1 = no2   #no1 =1,no1=1,no1=2,no1=3
    no2 = sum   #no2 =1,no2=2,no2=3,no2=5
    
    
    