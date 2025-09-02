#string[start:stop:step]
text = "PYTHONSTRING"
print(text[0:6])
print(text[6:])
print(text[:6])
print(text[:])
#print(text[]) error

print(text[::2]) #every 2nd char
print(text[1::2]) #1st index..
print(text[::3])

#reverse slicing
print(text[::-1])
print(text[::-2])
print(text[-1:-7:-1]) #pythonstring GNIRTS

#negative index
print(text[-1])
print(text[-6:-1])
print(text[-7:])
print(text[:-3])