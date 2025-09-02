sales = [122,23,45,66,77,89,901,23,556,77,89]

#even sales
#odd sales
#>200 elm

users =["ram","shyam","ram","seeta","geeta","seeta","parth"]
unique_list=[]
duplicate_list=[]

for i in users: #ram,ram
    if i not in unique_list: #ram
        unique_list.append(i) #ram
    else:
        duplicate_list.append(i)
            

print(unique_list)        
print(duplicate_list)

#[""ram,"seeta"]


