def order_food(func):#3
    def inner(person):#4
        if(person>0):#5
            print("Party is there",person)#6
            func(100)
        else:
            print("No party")
    return inner
@order_food#2
def throwing_party(persons):
    print("Party is for ",persons)
throwing_party(210)#1

#110 is being passed inside inner function
#func(100) will give value in throwing party becoz func=throwing_party
# throwing_part=order_food(throwing_party)