no1 = 100
no2 = 60 #30

max =0
if no1>no2:
    max = no1
else:
    max = no2

#max = 15        
lcm =0
while True:
    # 15 % 10 a==0 and 15 % 15 ==0 FALSE
    #16
    #20 % 10 == 0 and 20 % 15 =0 false
    #21,22,23,24,25
    #25% 10
    #30 % 10 ==0 and  30 % 15 ==0 yes
    
    if max % no1 ==0 and max %no2 ==0:
        lcm = max # lcm = 30
        break
    
    max+=1 #16 17

print(f" lcm of {no1} and {no2} = {lcm}")        
        