# def outer():
#     def inner():
#         print("Inner called")
#     inner()
# outer()
def outer():
    def inner():
        print("Inner is called")
    # inner()
    return inner
x=outer()
print(x)
x()