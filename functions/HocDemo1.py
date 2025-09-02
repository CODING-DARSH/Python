
def toBeCalled():
    print("to be called function called...")

def test(a):
    print(a) #toBeCalled -- address
    a()


# test(10)
# test("ok")
# test(False)    
# test([10,20])
test(toBeCalled)