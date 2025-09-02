def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(f"sum={sum}")
def sub(*args):
    total=0
    for i in args:
        total-=i
    print(f"sum={total}")
def mul(*args):
    total=1
    for i in args:
        total*=i
    print(f"sum={total}")
def div(*args):
    total=1
    for i in args:
        total/=i
    print(f"sum={total}")
def calc(op,*args):
    print(f"Calc is called")
    op(*args)
choice=input("Enter correct operation\n")

if choice=="add":
    print("Add funtion is called")
    calc(add,10,20,30,40,50)
elif choice=="sub":
    print("Subtraction funtion is called")
    calc(sub,10,20,30,40,50)
elif choice=="mul":
    print("Multiplication funtion is called")
    calc(mul,10,20,30,40,50)
elif choice=="div":
    print("Division funtion is called")
    calc(div,10,20,30,40,50)