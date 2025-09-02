# def checknum(func):
#     def inner(*args):
#         for i in args:
#             if type(i)==str:
#                 print(f"string found {i}")
#                 break
#             else:
#                 sum=0
#                 for i in args:
#                     sum+=i
#         print(f"{sum}")
#         func(*args)
#     # print(sum)
#     return inner
# @checknum
# def add(*args):
#     print("add is called")
# add(10,20,30,40)
# add(10,20,30,40,"raj")


def checknum(func):
    def inner(*args):
        sum = 0  
        for i in args:
            if type(i) == str:
                print(f"string found {i}")
                break
        else: 
            for i in args:
                sum += i
            print(f"{sum}")
        func(*args)
    return inner

@checknum
def add(*args):
    print("add is called")

add(10, 20, 30, 40)
add(10, 20, 30, 40, "raj")
