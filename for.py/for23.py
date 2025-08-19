#x,n=3,2
#f=1
#s=0
#for i in range(1,n+1):
#    f*=i
#    s+=x-x**i/f
#print(s)    
x,n=2,10
f=1
k=1
for i in range(3,n+1,2):
    f*=(i-1)*i
    print((-1)**k,f,2**i)
    k+=1
    pr
        
