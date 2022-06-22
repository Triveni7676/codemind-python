n=input()
r=len(n)
p=0
for i in range(0,r):
    if(n[i]>='0' and n[i]<='9'):
        #print(n[i])
        p=p+int(n[i])
print(p)
    