numbers = [100,20,34,56,77,121,56,790]

choice  = int(input("enter no to remove :"))
if choice in numbers:
    numbers.remove(choice)
else:
    print(f"{choice} is not avaialable in numbers")    
    #print("choice = ",choice)
    #print(f"choice  ={choice}")
    

print(numbers)    