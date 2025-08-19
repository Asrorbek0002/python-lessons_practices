from math import sin
a,b=0,2
n=2
h=(b-a)/n
print(h)
for i in range(n+1):
    x=a+h*i
    y=1-sin(x)
    print(y) 
