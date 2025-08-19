a,b,c=4.0,2.0,5.0
#a,b,c=1.2,2.1,4.6
if a<b<c:
    a,b,c=2*a,2*b,2*c
else:
    a,b,c=1/a,1/b,1/c
print(a,b,c)                    