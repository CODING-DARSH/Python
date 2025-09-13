data="I am darsh vithlani i am studying aiml in brindavan college"

data=data.lower()
data=data.split()
frequency={}
for i in data:
    if i not in frequency:
        frequency[i]=1
    else:
        frequency[i]+=1
print(frequency)