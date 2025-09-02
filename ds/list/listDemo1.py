#users =[] #empty list
users = ["ram","shyam","seeta","geeta","ajay","raj"]
print(users)
#print(type(users).__name__) string..

print(users[0])
print(len(users))

# for i in users:
#     print(i)

# for i in range(0,len(users)):
#     print(users[i])

users.append("arjun")
print(users)

users.extend(["poem","kavi"])
#users.extend("KAVI")

users.insert(2,"KRISHNA")
print(users)