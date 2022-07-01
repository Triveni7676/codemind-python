n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    temp=a[i]
    s=0
    while(a[i]>0):
        r=a[i]%10
        s=(s*10)+r
        a[i]=a[i]//10
    if(s==temp):
        c+=1
print(c)