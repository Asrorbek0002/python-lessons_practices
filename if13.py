a,b,c=4,2,6
if a>b:
    if b>c:
        print(b)
    elif a>c:
        print(c)
    else:
        print(a)
elif a>c:
    print(a)
elif b>c:
    print(c)
else:
    print(b)   
a,b,c=2,5,7
if a>b:
    if b>c:
        print(b)
    elif a>c:
        print(c)
    else:
        print(a)    
elif a>c:
    print(a)
elif b>c:
    print(c)
#else:
# 2-method
a,b,c=2,8,4    
if a>b>c or a<b<c:
    print(b)
elif b>a>c or b<a<c:
    print(a)  
else:
    print(c)              