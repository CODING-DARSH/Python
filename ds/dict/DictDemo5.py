scores ={"Virat":[90,101,34,78,120],"Rohit":[155,0,89,76,12]}

playerName = scores.keys()
print(playerName)

# for i,j in scores.items():
#     print(f"{i}",end=" ")
#     #j == list --> loop
#     for runs in j:
#         print(runs,end=" ")
#     print()    

finalScore = {}
sum=0
for i,j in scores.items():
    print(f"{i}",end=" ")
    #j == list --> loop
    for runs in j:
        print(runs,end=" ")
        sum = sum + runs
    finalScore[i] =sum
    sum =0
    print()    

print(finalScore)    