n=input()
r=len(n)
v=0
c=0
d=0
s=0
for i in range(0,r):
    if n[i] in 'AEIOUaeiou':
        v+=1
    elif n[i]>='0'and n[i]<='9':
        d+=1
    elif n[i]==' ':
        s+=1
    else:
        c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",s)