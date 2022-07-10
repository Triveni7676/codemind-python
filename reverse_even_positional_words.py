n=input()
l=[]
c=0
for i in n.split():
    if c%2==0 or c==0:
        print(i[::-1],end=' ')
    else:
        print(i,end=' ')
    c+=1