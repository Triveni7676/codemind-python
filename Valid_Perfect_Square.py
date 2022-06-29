a=int(input())
for i in range(a):
    b=int(input())
    for j in range(1,b+1):
        k=j*j
        if(b==k):
            print("True")
            break
    else:
        print("False")