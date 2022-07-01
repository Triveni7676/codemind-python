n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=[]
p=sorted(set(b))
c=0
for i in range(len(a)):
    for j in range(len(p)):
        if(a[i]==p[j] and a[i]!=-1):
            p[j]=-1;
            c+=1
print(c)