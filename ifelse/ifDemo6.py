age = int(input("enter age:"))

if age>=18:
    print("user is eligible of driving bike and car")
    if age>21:
        print("user is eligible for marrige")
    else:
        print("user is not eligible for marrige.")    
    
else:
    print("user is not eligible for driving bike and car...")
    if age>=16:
        print("user is eleigible to drive EV")    
    elif age>=10:
        print("user is eleigible to drive cycle")    
    else:
        print("stay at home...")    
            
