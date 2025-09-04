# def getsudents(*names):/
    # print(names)
# getsudents("dars","shyam")/

# def pdfhandler():
#     print("pdf handler is called")
# def imagehandler():
#     print("Image handler is called")
# def dochandler():
#     print("Image handler is called")

# def filehandler(a): #a==imagehandler
#     a() #imagehandler()
# filename="abc.pdf"
# if filename.endswith(".jpg"):
#     filehandler(imagehandler)   #filehandler is beig called 
# elif filename.endswith(".pdf"):
#     filehandler(pdfhandler)
# elif filename.endswith(".doc"):
#     filehandler(dochandler)

# def data(x,**kwargs):
#     print(kwargs)
# data(x=10,name="Darsh",age=12,weight=90)

#============================================================================================

#---->lambda function

# x=lambda a:print(f"{a}")
# x(10)

# name=lambda fname,lname:print(f"{fname}-{lname}")
# name("Darsh","Vithlani")

# to find whether number are even or not using lambda

# x=lambda a: "even" if a%2==0 else "odd"
# print(x(2)) 

# numbers=[10,20,30,40,50]
# sqnumbers=map(lambda i:i**2,numbers)
# print(list(sqnumbers))

# data=["ram","shyam","lakhan","sita"]
# UpperCase=map(lambda x:x.upper(),data)
# print(list(UpperCase))

# users = ["naman","sumit","bob","raj","jay","madam","sanjay"]
# sorted=map(lambda x:x.upper(),filter(lambda y:y.startswith("s"),users))
# print(list(sorted))

for i in range(1,10,+2):
    print(i)