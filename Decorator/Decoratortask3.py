#wap to make a bank account witdrawl system using decorator
def withdrawl(func):
    def process(username,availamount,password,withdrawlam):
        if username=="darsh" and password=="darsh@123":
            print("Your account details are as follows\n")
            print(f"balance available in ur amount is {availamount}")
            if availamount==0 or availamount<withdrawlam:
                print("Insufficient balance given amount cant be withdraw")
            else:
                print(f"{withdrawlam} is successfully withdrawed")
                print(f"Total available balance after withdrawal {availamount-withdrawlam}")
            func(username,availamount,password,withdrawlam)
        else:
            print("Incorrect password")
    return process        

@withdrawl
def bank(username,availamount,password,withdrawlam):
    print("Bank function is called successfully")
# bank("darsh",15000,"darsh@123",10000)
bank("darsh",15000,"Darsh@123",10000)


