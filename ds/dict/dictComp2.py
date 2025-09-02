users = ["ram","shyam","bob","naman","ajay","madam","jay"]

data = {i:len(i) for i in users if len(i)>3}
print(data)

paln = {i:len(i) for i in users if i==i[::-1]}
print(paln)

palnflag = {i:"yes" if i==i[::-1] else "No" for i in users}
print(palnflag)

numbers = [12,22,34,55,-15,0,78,-90,123]
even_odd= {i:"even" if i %2==0 else "odd" for i in numbers}
print(even_odd)

#pos_neg = {i:"pos" if i>0 else "Neg" for i in numbers}
pos_neg = {i:"pos" if i>0 else ("zero" if i ==0 else "Neg") for i in numbers}
print(pos_neg)