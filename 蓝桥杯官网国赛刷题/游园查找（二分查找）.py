
s = input()
sub = ''
person = []
for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        if sub != '':
            person.append(sub)
        sub = s[i]
    else:
        sub += s[i]
person.append(sub)

from bisect import bisect_left
l=len(person)
h=[None]
p=[None]*l
b=['']
for i in range(l):
    if b[-1]<person[i]:
        p[i]=h[-1]
        b.append(person[i])
        h.append(i)
    else:
        k=bisect_left(b,person[i])
        b[k]=person[i]
        h[k]=i
        p[i]=h[k-1]
ans=[]
q=h[-1]
while q is not None:
    ans.append(person[q])
    q=p[q]
ans=''.join(ans[::-1])
print(ans)