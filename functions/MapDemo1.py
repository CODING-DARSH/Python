#list , (), {} numric  --> 10,20,30 -- 100,...

numbers = [10,20,30,40,50]
#sqNumbers = [i **2 for i in  numbers]

# for i in numbers:
#     sqNumbers.append(i**2)

#print(sqNumbers)    

#map function

#map -- loop --numbers --1,1,1, -- x  x**2
sqNumbers = map(lambda x:x**2,numbers)
#sqNumbers = map(lambda x:x>10,numbers)
print(list(sqNumbers))

users = ["ram","shyam","amit","sumit","suthar"]

upperUser = map(lambda x: x.upper(),users)
print(list(upperUser))

#sales = [1000,1200,3400,7000,8900,600]
#profit = 10%[1100,....]