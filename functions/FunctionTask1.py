def flex_math(op,*args):
    ans =0
    ans1 =1
    match op:
        case "add":
            for i in args:
                ans = ans+i
            return ans
        case "mul":
            for i in args:
                ans1 = ans1*i
            return ans1    

x = flex_math("mul",1,2,3,4)        
print(x)
                
        