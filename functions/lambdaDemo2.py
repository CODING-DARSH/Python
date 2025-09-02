findMax = lambda a,b: a if a>b else b
print(findMax(100,20))

posneg = lambda x : "pos" if x>0 else "neg"
print(posneg(-100))


palndrome = lambda name: "pal" if name == name[::-1] else "not paln"
print(palndrome("namana"))

findMaxPro = lambda a,b,c :a if (a>b and a>c) else (b if b>c else c)
print(findMaxPro(10,200,30))

posnegpro = lambda x : "pos" if x>0 else("zero" if x ==0 else "neg")
print(posnegpro(10))
