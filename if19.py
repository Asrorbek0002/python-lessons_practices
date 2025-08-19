#a,b,c,d=8,4,5,2
#x = a%2 + b%2 + b%2 + d%2
#tr = 0
#if x==3:
#    q = 0
#else:
#    q = 1
#if a%2==q:
#    tr = 1
#elif b%2==q:
#    tr = 2
#elif c%2==q:
#    tr = 3
#elif d%2==q:
#    tr = 4
#print(tr)


#if a%2==b%2==c%2!=d%2:
#    print(4)
#if a%2==b%2!=c%2==d%2:
#    print(4)
#if a%2==b%2==c%2!=d%2:
#    print(4)
#if a%2==b%2==c%2!=d%2:
#    print(4)
a,b,c,d=9,2,5,7
a,b,c,d=a%2,b%2,c%2,d%2
x=a%2+b%2+c%2+d%2
#tr=0
if x==3:
    q=0
else:
    q=1
if a%2==q:
    print(1)
elif b%2==q:
    print(2)
elif c%2==q:
    print(3)
elif d%2==q:
    print(4)            
a,b,c,d=9,5,4,1
if a%2==b%2==c%2!=d%2:
    print(4)
elif a%2==b%2==d%2!=c%2:
    print(3)
elif a%2==c%2==d%2!=b%2:
    print(2)
elif b%2==c%2==d%2!=a%2:
    print(1)        

      