#n=2
#s=0
#for i in range(11,20,2):
#    s+=i/10
#print(s)
#a=0
#for i in range(12,20+1,2):
#   a-=i/10
#print(a)
#x=s+a
#print(x)        
#d=0
#for i in range(12,20+1,2):
#print(d)        
n=2 
s=0
for i in range(1,n+1):
    s+=((-1)**(i+1)*(1+i/10))
print(s)    
