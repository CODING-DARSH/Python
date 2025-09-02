sales = [[100,120],[110,150],[120,200]]

print(sales)
# print(sales[0])
# print(sales[0][0])

# for i in range(0,len(sales)):
#     #print(sales[i]) #[100,120]
#     for j in range(0,len(sales[i])):
#         print(sales[i][j],end=" ")
#     print()     

# for i in sales:
#     for j in i:
#         print(f"{j}",end=" ")
#     print()    

for i,j in sales:
    print(f"{i}  {j}",end=" ")