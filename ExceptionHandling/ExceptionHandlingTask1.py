# data=[10,20,30,40]
# data.remove(50)
# # print(f"data1 is being removed {data1}")
# print(data)

try:
    data=[10,20,30,40]
    data.remove(50)
    print(data)
except ValueError as v:
    # print("Value isnt there in list")
    print(v)