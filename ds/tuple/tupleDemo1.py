# data =() #empty tuple

# print(data)
# print(type(data))

data = ("ram","shyam","amit","sumit","ram")
print(data)

print(data[0])

for i in data:
    print(i)
    
cnt = data.count("ram")
print(cnt)

ind = data.index("amit")
print("index ",ind)