n=int(input())
e=0
o=0
arr=list(map(int,input().split()))
for i in arr:
    if i%2==0:
        e+=1
    else:
        o+=1
print(e,o)