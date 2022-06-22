n=int(input())
a=[]
a=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(j!=i and a[j]<a[i]):
            c+=1
    print(c,end=' ')