a,b,c=4,2,6
if a>b:
    if b>c:
        print(a+b)
    elif a>c:
        print(a+c)
    else:
        print(c+a)
else:
    if a>c:
        print(a+b)
    elif b>c:
        print(b+c)
    else:
        print(b+c)                        