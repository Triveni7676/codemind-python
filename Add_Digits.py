n=int(input())
s=0
if(n<10):
    print(n)
else:
    while(n>9):
        s=0
        while(n>0):
            r=n%10
            s=s+r
            n=n//10
        n=s
    print(s)