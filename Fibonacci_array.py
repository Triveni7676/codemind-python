n=int(input())
a=list(map(int,input().split()))
k=0
c=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(i+2,n):
            if(a[i]+a[j]==a[k]):
                c+=1
if(k-1==c):
    print("yes")
else:
    print("no")