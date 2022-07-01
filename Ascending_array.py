n=int(input())
a=list(map(int,input().split()))
k=0
c=0
max=0
for i in range(n):
    k+=1
    if(a[i]>max):
        max=a[i]
        c+=1
if(c==k):
    print('yes')
else:
    print("no")