n=int(input())
s=0
sum1=0
sq=n*n
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
res=s*s
while(res>0):
    r=res%10
    sum1=sum1*10+r
    res=res//10
if(sq==sum1):
    print("True")
else:
    print("False")
    