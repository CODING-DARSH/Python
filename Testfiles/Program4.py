def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1//num2

def operation(op,num1,num2):
    ans=op(num1,num2)
    print(ans)
choice=int(input("1] Add \n 2] Sub \n 3] Mul \n 4] Div \n Enter ur choice:"))
match choice:
    case 1:
        operation(add,10,20)
    case 2:
        operation(sub,10,20)
    case 3:
        operation(mul,10,20)
    case 4:
        operation(div,10,20)
    case _:
        print("Enter valid choice")

