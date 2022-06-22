import math
n=int(input())
a=[]
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    temp=a[i]
   # print(temp)
    p=math.sqrt(a[i])
   # print(p)
    k=int(p)*int(p)
    #print(k)
    r=temp-k
    if(r==0):
        s=s+a[i]
print(s)
    
    