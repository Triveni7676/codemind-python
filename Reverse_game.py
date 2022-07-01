n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    s=0
    while(a[i]>0):
        r=a[i]%10
        s=(s*10)+r
        a[i]=a[i]//10
    print(s,end=' ')