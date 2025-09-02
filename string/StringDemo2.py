data = "hi this is india"
count=0
for i in data:
    if " " in i:
        count+=1

print(f"count = {count}")        