# sp ending point sum

sp = int(input("enter sp :"))
ep = int(input("enter ep :"))
sum=0
for i in range(sp,ep+1):
    sum = sum + i
    print(i,end=" ")

print("sum = ",sum)    