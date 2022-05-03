n=int(input())
sum=0
res=1
while(n>0):
    r=n%10
    sum=sum+r
    res=res*r
    n=n//10
if(sum==res):
    print("Spy Number")
else:
    print("Not Spy Number")

    