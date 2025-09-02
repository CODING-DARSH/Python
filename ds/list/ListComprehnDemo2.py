data = [11,22,232,45,67,887,65,43,126]
#even no
evenList =[i for i in data if i %2 ==0]

# for i in data:
#     if i %2==0:
#         evenList.append(i)

print(evenList)        


users = ["ram","ramesh","shyam","seeta","ajay","raj","rahul"]
#rstart..
rlist =[i for i in users if i.startswith("r")]

# for i in users:
#     if i.startswith("r"):
#         rlist.append(i)

print(rlist)        