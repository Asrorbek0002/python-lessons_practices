a,b,c=5,4,5
x=(a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)
print(x)
a,b,c=5,5,5
x=(a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)
print(x)