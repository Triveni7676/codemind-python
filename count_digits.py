n=int(input())
a=list(map(int,input().split()))
print
p=[]
k=0
for i in range(n):
    c=0
    if(a[i]==0):
        c=1
    if(a[i]<0):
        a[i]=abs(a[i])
       # print(a[i])
    while(a[i]>0):
        r=a[i]%10
        c+=1
        a[i]=a[i]//10
    print(c,end=' ')
  