n=int(input())
a=list(map(int,input().split()))
max=0
p=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(a[i]==a[j]):
            c+=1
    if(c==1):
        if(a[i]>max):
            max=a[i]
            p+=1
if(p>0):
    print(max)
else:
    print('-1')