a,b=15,25
if (a!=b and a>b):
   a,b=a,a
elif (a!=b and a<b):
   a,b=b,b   
else:
   a=b=0
print(a,b)      

   