a,b,c=50,20,40
if a>b:
    if b>c:
        a=a-b
        print(b,a)
    elif a>c:
        a=a-c
        print(c,a)
    else:
        c=c-a
        print(a,c)
else:
    if a>c:
        b=b-a
        print(a,b)
    elif b>c:
        b=b-c
        print(c,b)
    else:
        c=c-b
        print(b,c)                         