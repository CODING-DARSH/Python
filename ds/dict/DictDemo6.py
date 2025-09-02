itinerary = {"Uk":{"London":"Palce","Bermighum":"Stadium"},"France":{"paris":"Effile Tower","kanns":"Ramp wok"}}

print(itinerary)
k = itinerary.keys()
print(k)

for i,j in itinerary.items():
    print(i,end=" ")
    print(j) #j == dict
    for a,b in j.items():
        print(a,end=" ")
        print(b)
    