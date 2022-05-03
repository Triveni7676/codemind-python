import math
a,b,c=map(int,input().split())
p=math.pow(a,b)
sum=p%c
print(int(sum))