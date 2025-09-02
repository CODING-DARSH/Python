#{1:1,2:2,3:3,4:4,5:5}

#data ={}

# for i in range(1,6):
#     data[i]=i

data = {i:i**2 for i in range(1,6)}
print(data)    

users = ["ram","shyam","amit","sumit","ajay","raj","jay"]
#{"ram":3}

data1 = {i:len(i) for i in users}
print(data1)

data2 ={i[0]:i for i in users}
print(data2)


sales =[100,200,300,400,500,600,700]
#{100:90}

salesandprofit  ={i:i-i*0.1 for i in sales}
print(salesandprofit)

