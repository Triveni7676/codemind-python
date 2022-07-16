n=input()
a=0
lower=set('abcdefghijklmnopqrstuvwxyz')
for i in range(len(n)):
    if n[i] in lower:
        k=n.count(n[i])
        if(k==1):
            a+=1
print(a)