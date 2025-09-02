name="royal"
#upper..
name = name.upper() #new ref
print(name)
name = name.lower()
print(name)

sent = "hi this is india"
#sent = sent.capitalize()
sent = sent.title()
print(sent)

sent1 = "Hi tHIs Is iNdIa"
sent1 = sent1.swapcase()
print(sent1)

email = "  samir@gmail.com   "
print(email)
print("before",len(email))

#remove white space...
#email =email.lstrip()
#email =email.rstrip()
email = email.strip()
print(email)
print("after",len(email))

