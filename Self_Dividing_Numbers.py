def is_self(n):
    c=0
    k=0
    temp=n
    while(n!=0):
        r=n%10
        if r==0:
            return 0
        elif temp%r==0:
            c+=1
        k+=1
        n//=10
    if c==k:
        return 1
    return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if is_self(i):
        print(i,end=' ')