n=int(input())
large=0
while(n>0):
    r=n%10
    if(r>large):
        large=r
    n=n//10
print(large)        

    