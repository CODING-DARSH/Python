# users=[]
# users=["ram","lakhan","seeta"]
# print(len(users))
# print(type(users))
# for i in users:
    # print(i)

# users.append("Arjun")
# print(users)

# users.extend(["poem","kavi"])
# print(users)
# users.insert(2,"ravan") #at 2nd position means after lakhan it will insert ravan
# print(users)

# while True:
    # name=input("Enter name or exit")
    # if name=="exit":
        # break
    # else:
        # users.append(name)
# print(users)

# users.pop(0)
# # print(removename)
# # print(users)

# data=[[100,110],[120,130],[140,150]]

# for i,j in data:
#     print(i,j)

# data = [[10,20,30],[10,30,30],[10,20,20]]
# #data =[60,70,50]
# x=[]
# for i in data:
#     sum=0
#     for j in i:
#         sum+=j
#     x.append(sum)
# print(x)



# scores = [["virat",100,71,91],["rohit",90,80,20],["ms",20,111,90]]
# #ouput: [["virat",total],["rohit",total],["ms",total]]

# output=[]
# name=""
# for i in scores:
#     total=0
#     name=i[0]
#     for j in range(1,len(i)):
#         total+=i[j]
#     output.append([name,total])
# print(output)



# marks =[["ram",18,19,20],["ajay",19,19,17],["shyam",22,23,22]]
# # output = [["ram",total,per],["ram",total,per],["ram",total,per]]

# name=""
# output=[]
# for i in marks:
#     name=i[0]
#     total=0
#     percentage=0
#     for j in range(1,len(i)):
#         total+=i[j]
#         percentage=round(total/3,2)
#     output.append([name,total,percentage])
# print(output)


#reverse a string 


# reversed=[]
# data=[10,20,30,40,50]
# # for i in range(4,-1,-1):
#     # reversed.append(data[i])
# # print(reversed)
# n=len(data)
# print(n)
# for i in range(n//2):
#     print(i)
#     data[i],data[n-i-1]=data[n-i-1],data[i]    #10,50=50,10 ===> 20,40=40,20        ==>0,4=4,0    ===>1,3=3,1
# print(data)

#remove duplicate names from list


# data=["ram","lakhan","sita","laxman","ram","sita","darsh"]
# new_data=[]
# for i in data:
#     if i not in new_data:
#         new_data.append(i)
# print(new_data)



data = [1, 2, 7, 8, 4]
data1 = [4, 6, 1, 3, 2]
new_data=[]
for j in range(len(data)):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
for j in range(len(data1)):
    for i in range(len(data1)-1):
        if data1[i] > data1[i+1]:
            data1[i], data1[i+1] = data1[i+1], data1[i]

for i in data:
    new_data.append(i)
for i in data1:
    new_data.append(i)
print(data)
print(data1)
print(new_data)

for i in range(len(new_data)):
    for j in range(len(new_data)-1):
        if new_data[j]>new_data[j+1]:
            new_data[j],new_data[j+1]=new_data[j+1],new_data[j]
print(new_data)