n=int(input())
odd=0
arr=list(map(int,input().split()))[:n]
for i in range(0,n):
    if(arr[i]%2!=0):
        odd+=1;
if(odd<=2):
    print("YES")
else:
    print("NO")