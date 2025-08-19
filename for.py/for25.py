x,n=3.0,2
f=1
s=0
for i in range(1,n+1):
    s+=x-x**i/i
print(int(s))    