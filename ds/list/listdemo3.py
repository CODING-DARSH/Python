#remove...

numbers = [100,20,34,56,77,121,56,790]
print(numbers)

#removedElm = numbers.pop() #it will remove last elm
removedElm = numbers.pop(3) #it will remove last elm
print("remving....",removedElm)
print(numbers)

numbers.remove(77) #ValueError: list.remove(x): x not in list
print(numbers)