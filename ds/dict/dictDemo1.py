# data ={}
# print("data",data)
# print(type(data).__name__)

data ={"Gujarat":"Gandhinagar","Maharashtra":"Mumbai","Rajasthan":"Jaipur","Gujarat":"Ahmedabad"}
print(data)
data["Wb"]= "Kolkatta"
print(data)
data.update({"Up":"Lucknow","Karntaka":"Banglore"})
print(data)

#subscrip....
#print(data["Rajasthan"]) #key error Rajasthan1
if "Rajasthan1" in data:
    print(data["Rajasthan1"])
else:
    print("no key available...")
    

print(data.get("Gujarat"))    


#iteration

k = data.keys()
print(list(k))

v = data.values()
print(v)

kv = data.items()
print(kv)
# [('Gujarat', 'Ahmedabad'), ('Maharashtra', 'Mumbai'), ('Rajasthan', 'Jaipur'),
# ('Wb', 'Kolkatta'), ('Up', 'Lucknow'), ('Karntaka', 'Banglore')]

#i = key
#j =value
for i,j in data.items():
    print(i,j)

