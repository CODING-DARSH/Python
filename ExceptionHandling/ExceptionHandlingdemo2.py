# users = ["rama","shyam","ammit","sumit"]

# try:
#     if "ram" not in users:
#         raise ValueError("ram must present in list")
# except ValueError as e:
#     print(e)




class ValueCheckException(Exception):
    
    def __init__(self, *args):
        super().__init__(*args)        


users = ["rama","shyam","ammit","sumit"]

try:
    if "ram" not in users:
        raise ValueCheckException("ram must present in list")
except ValueCheckException as e:
    print(e)  