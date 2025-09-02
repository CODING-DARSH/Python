age = 19
age1 = 20

# print("age = ",age)
#print(f"age = {age} age1 = {age1}")


choice = int(input(f" press 1 for add\n press 2 for sub\n press 3 for div\n press for mul "))

match choice:
    case 1:
        #break
        no1 = int(input("enter no1 :"))
        no2 = int(input("enter no2 :"))
        ans = no1 + no2
        print(f"no1 = {no1} no2 = {no2} ans = {ans}")
    case 2:
        no1 = int(input("enter no1 :"))
        no2 = int(input("enter no2 :"))
        ans = no1 - no2
        print(f"no1 = {no1} no2 = {no2} ans = {ans}")
    case _:
        print("invalid choice...")    
        
            