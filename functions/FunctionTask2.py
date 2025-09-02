def smart_print(*args,sep=" ",end="\n" ,upperCase=False):
    op = sep.join(args)
    if upperCase==True:
        op = op.upper()
    
    print(op)        

smart_print("Hello","world","hi",sep="-",upperCase=True)    
