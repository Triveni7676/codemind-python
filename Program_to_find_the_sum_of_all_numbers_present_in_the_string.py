n=input()
r=len(n)
s=0
for i in range(0,r):
    if n[i] in '1234567890':
        s=s+int(n[i])
print(s)