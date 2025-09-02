# with open("th.txt","r") as file1:
#     x=file1.read()
#     print(x)

# with open("th.txt","r") as file2:
#     x=file2.readline()
#     print(x)

# with open("th.txt","r") as file2:
#     x=file2.readline(10)
#     print(x)

# with open("th.txt","r") as file3:
#     # x=file3.readline()
#     while True:
#         x=file3.readline()
#         print(x,end="")
#         if not x:
#             break

# with open("th.txt","r") as file4:
#     x=file4.readlines()
#     print(x)

with open("th.txt","r") as file4:
    for i in file4.readlines():
        print(i,end="")