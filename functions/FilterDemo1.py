numbers = [12,22,33,45,32,121,78,90,99,87,66]

# x%2==0 prediate -- true false...
evenNos = filter(lambda x: x%2==0,numbers)
print(list(evenNos))

users = ["naman","sumit","bob","raj","jay","madam","sanjay"]

palindromes = filter(lambda x:x==x[::-1],users)
print(list(palindromes))

snames = filter(lambda x:x.startswith("s"),users)
print(list(snames))