filename = "report.pdf"

ext = filename[-3:]
print(ext)


mobile = "8460224296"
masked = "******"+mobile[-4:]
print(masked)

email = "samir@gmail.com"
# #index... @
# ind = email.index("@")
# print(ind)

# domain = email[ind+1:]
# print(domain)

domain = email[email.index("@")+1:]
print(domain)