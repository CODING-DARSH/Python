#123 - no of digit 3

'''
    123 /10 ->12
    12/10 -->1
    1/10 -->0
    
    4532/10 = 453
    453/10 45
    45 / 10 4
    4/10  0
'''



no = 123
count=0

while no>0:
    no = no // 10
    #print(no)
    count+=1
    
print("count = ",count)    

#print(10//5)