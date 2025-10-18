from math import *
a=10
b=99
c=[]
for i in range(a,b+1):
    for j in range(2, int(sqrt(i))+1):
        if i%j==0:
            break
        else:
            c.append(i)
print(*set(c))
            
        
