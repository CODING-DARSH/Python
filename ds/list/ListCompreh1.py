#[1,2,3,4,5]
# x =[]
# for i in range(1,6):
#     x.append(i)

x = [i for i in range(1,6)]
print(x)    

data = [1,2,3,4,5]
#sqlist=[1,4,9,16,25]
sqllist =[i**2 for i in data]

# for i in data:
#     sqllist.append(i**2)
print(sqllist)    


names =["raj","parth","shyam","sundar","amit"]
#upperName = ["RAJ".....]
upperName =[i.upper() for i in names]

# for i in names:
#     upperName.append(i.upper())
print(upperName)    

initalchar = [i[0] for i in names]
print(initalchar)