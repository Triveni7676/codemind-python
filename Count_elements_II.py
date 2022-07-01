a,b=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=set(p)
#print(r)
t=set(q)
#print(t)
c=0
x=list(r)
v=list(t)
for i in x:
    if i not in v:
        c+=1
for i in v:
    if i not in x:
        c+=1
print(c)
#print(v)
# for i in range(len(x)):
#     for j in range(len(v)):
#         if(x[i]!=v[j]):
#             c+=1
# print(c)
        