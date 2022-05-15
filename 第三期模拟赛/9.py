n,m,k = map(int,input().split())
import time

a = []
for i in range(n):
    a.append(list(map(int,input().split()))+[i])

s = [0]*n
for i in range(m):
    a.sort(key=lambda x:x[i])
    #a = sorted(a,key=lambda x:x[i])
    for j in range(n):
        s[a[j][-1]] += j
print(' '.join(map(str,s)))

