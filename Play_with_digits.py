n=int(input())
a=list(map(int,input().split()))
#print(a)
s=0
for i in range(n):
    while(a[i]>0):
        r=a[i]%10
        s=s+r
        a[i]=a[i]//10
print(s)