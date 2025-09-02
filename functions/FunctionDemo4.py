# def findMax(*args):
#     m = args[0]
#     for i in args:
#         if i>m:
#             m = i
#     return m

def findMax(*args):
    return max(args,key=len)


#maxNo = findMax(10,20,200,333,456,78)
maxString = findMax("ram","shyam","amit","sumit","ajay","malayalam")
#print(f"maxno = {maxNo}") 
print(f"max string = {maxString}")

