n=int(input())
p=1
res=0
while n>0:
    r=n%10
    p=p*r
    res=res+r
    n=n//10
area=p-res
print(area)
    