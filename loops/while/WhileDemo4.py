
#123
no = int(input("enter no "))
sum =0
rev=0
while no>0:
    rem = no % 10 #3 2 1
    rev = (rev*10)+rem  # rev = (0*10)+3 = 3 #3 = (3*10)+2 32= 32*10+1 = 320+1 = 321
    no = no //10   #12 1


print(f"rev no = {rev}")    
    
    
