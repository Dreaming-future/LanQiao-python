
from collections import defaultdict,deque

d = defaultdict(int)
n = int(input())
tree = defaultdict(list)
        

for _ in range(n):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    d[a] += 1
    d[b] += 1

q = deque([])
used = defaultdict(int)
for i,j in d.items():
    if j == 1:
        used[i] = 1
        q.append(i)

while q:
    u = q.popleft()
    for v in tree[u]:
        if not used[v]:
            d[v] -= 1
            if d[v] == 1:
                q.append(v)
                used[v] = 1
                
res = []
for i,j in d.items():
    if j != 1:
        res.append(i)
res.sort()
print(" ".join(map(str,res)))
