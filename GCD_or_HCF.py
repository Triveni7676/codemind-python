a,b=map(int,input().split())
large=0
for i in range(1,b):
    if(a%i==0 and b%i==0):
        if(i>large):
            large=i
print(large)