numbers = [12,22,34,55,15,78,90,123]

remdict ={}
for i in numbers:
    rem = i % 2
    if rem in remdict:
        remdict[rem].append(i)
    else:
        remdict[rem]=[i]    

print(remdict)        