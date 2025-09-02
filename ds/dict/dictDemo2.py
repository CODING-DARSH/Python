data = {1001:"Ram",2003:"Ramesh",5004:"ajay",1007:"kunal"}
print(data)
removedValue = data.pop(5004) #error..
print(f"remving....{removedValue}")
print(data)

#data.clear() #empty...
remvoveData = data.popitem() # you have to check key len of dict...
print(f"removing..{remvoveData}")
print(data)


