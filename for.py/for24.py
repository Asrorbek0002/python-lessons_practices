x,n=2.0,1
s=0
f=1
for i in range(1,n+1):
    f*=i
    s+=1-x**i/f
print(int(s))
