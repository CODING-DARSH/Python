name = "royal is A institute"

count=0
# for i in name:
#     if i == 'a' or i == 'e' or i =='o' or i=='i' or i =='u':
#         count+=1


vovels = "aeiouAEIOU"
for i in name:
    if i in vovels:
        count+=1
    
print(f"count = {count}")        