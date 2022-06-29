

n=int(input())
c=0
k=0
j=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if(c==2):
    while n:
         s=0
         r=n%10
         j+=1
         for i in range(1,r+1):
            if(r%i==0):
                s+=1
            if(s==2):
                k+=1
         n=n//10
    if(k==j):
        print("Mega Prime")
    else:
       print("Not Mega Prime")        
else:
    print("Not Mega Prime")
        