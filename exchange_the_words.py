n=input()
l=[]
c=0
x=[]
for i in n.split():
    l.append(i)
for i in l:
    x.insert(0,i)
print(*x)