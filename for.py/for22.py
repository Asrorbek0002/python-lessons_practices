x,n=2,2
f=1
s=0
for i in range(1,n+1):
     f*=i
     s=1+x+x**i/f
print(s)     