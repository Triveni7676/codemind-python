n=input()
a=[]
lower=set('abcdefghijklmnopqrstuvwxyz')
for i in range(len(n)):
    if n[i] in lower:
        k=n.count(n[i])
        if(k==1):
            a.append(n[i])
print(''.join(sorted(a)))
        