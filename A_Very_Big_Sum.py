n=int(input())
s=0
a=[]
a=list(map(int,input().split()))
for i in range(0,n):
    s=s+a[i]
print(s)