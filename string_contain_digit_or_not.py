n=input()
r=len(n)
c=0
for i in range(0,r):
    if(n[i]>='0' and n[i]<='9'):
        c+=1
if(c!=0):
    print('Contains',c,'digit')
else:
    print("Doesn't contain digit")