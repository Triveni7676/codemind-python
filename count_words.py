def count_words(s):
    vowel=set("aeiouAEIOU")
    c=0
    for i in s.split():
        i=list(i)
        n=len(i)-1
        if i[0] in vowel and i[n] not in vowel:
            c+=1
    return c
s=input()
print(count_words(s))