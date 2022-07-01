n=int(input())
a=list(map(int,input().split()))
p=[]
k=0
for i in range(n):
    c=0
    while(a[i]>0):
        r=a[i]%10
        c+=1
        a[i]=a[i]//10
    #print(c)
    p.append(c)
x=min(p)
y=p.count(x)
print(y)