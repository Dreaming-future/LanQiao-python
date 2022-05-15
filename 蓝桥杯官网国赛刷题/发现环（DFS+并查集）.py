
from collections import defaultdict
used = defaultdict(int)
tree = defaultdict(list)

def get_father(x):
    if father[x] != x:
        father[x] = get_father(father[x])
    return father[x]

def union(x,y):
    fatherx, fathery = get_father(x), get_father(y)
    if fatherx != fathery:
        father[fatherx] = fathery

n = int(input())
father = [i for i in range(n+1)]

ans = [0]*(n+1)
def dfs(pos, idx):
    ans[idx] = pos
    if pos == end:
        res = sorted(ans[:idx+1])
        print(" ".join(map(str,res)))
        return
    for v in tree[pos]:
        if not used[v]:
            used[v] = 1
            dfs(v,idx+1)
            used[v] = 0
            

for _ in range(n):
    a,b = map(int,input().split())
    fa,fb = get_father(a),get_father(b)
    if fa == fb:
        start,end = a,b
        # break
    else:
        union(a,b)
        tree[a].append(b)
        tree[b].append(a)

used[start] = 1
dfs(start,0)