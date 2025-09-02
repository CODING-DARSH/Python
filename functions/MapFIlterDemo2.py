users = ["naman","sumit","bob","raj","jay","madam","sanjay"]

# sname = filter(lambda x:x.startswith("s"),users)
# uppernName = map(lambda x:x.upper(),sname)
#print(list(uppernName))

upperSname = map(lambda x:x.upper(),filter(lambda x:x.startswith("s"),users))
print(list(upperSname))

#numnwe -- even no sq