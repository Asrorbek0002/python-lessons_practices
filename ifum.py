a,b,c=4,2,6
if a>b:
    if b>c:
        x=a+b
    elif a>c:
        x=a+c
    else:
        x=a+c
else:
    if a>c:
        x=b+a
    elif b>c:
        x=b+c
    else:
        x=b+c
print(x)                                
