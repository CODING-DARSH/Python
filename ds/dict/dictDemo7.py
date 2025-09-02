words = ["hi","hello","AI","python","world","a"]

len_dict={}

for w in words:
    #print(w)
    l =len(w) # 2 ,5,2,6,5 #
    #print(l)
    #w = hi l = 2
    #w = hello l = 5
    #w = ai l =2
    #2 in {} -False
    #5 in {} =false
    #2 in {} =True
    if l in len_dict:
        #{2:["hi","AI"]}
        len_dict[l].append(w)
    else:
        #{2:["hi"],5:["hello"]}
        #
        len_dict[l] = [w]

print(len_dict)            
    

    