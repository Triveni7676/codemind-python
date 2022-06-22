t=int(input())
l=[]
c=0
for i in range(t):
    a=int(input())
    l.append(a)
n=int(input())
for i in range(len(l)):
    if l[i]<=n:
        c+=1
    else:
        c+=2
print(c)