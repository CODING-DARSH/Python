def order_food(func):#func=throwing party 3
    def inner():#4
        print("Ordering food")#5
        func()
    return inner
@order_food#2
def throwing_party():
    print("Throwing party.....")
throwing_party()#1

