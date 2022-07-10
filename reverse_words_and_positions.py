s=input()
x=s.split(' ')
y=' '.join(reversed(x))
l=[]
x=y[::-1]
for i in x.split():
    l.append(i)
for i in range(len(l)-1,-1,-1):
    print(l[i],end=' ')