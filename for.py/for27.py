x,n=0.5,2
f1=1
f2=1
s=x
for i in range(1,n+1):
    f1*=2*i-1
    f2*=2*i
    s+=(f1*x**(2*i+1))/(f2*(2*i+1))
    print(f1,f2,x**(2*i+1),(2*i+1))