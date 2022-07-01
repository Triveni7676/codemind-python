n=int(input())
a=list(map(int,input().split()))
k=0
for i in a:
    i=str(i)
    x=len(i)
    if x>k:
        k=x
for i in a:
    i=str(i)
    if len(i)==k:
        print(i,end=' ')