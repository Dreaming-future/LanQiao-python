'''
https://www.lanqiao.cn/problems/1124/learning/
难度: 简单   标签: Kruskal, Prim
'''

n,m = map(int,input().split())
# graph = [[0]*(n+1) for _ in range(n+1)]
edge = []
for _ in range(m):
    u,v,w = map(int,input().split())
    edge.append((u,v,w))


f = [i for i in range(n+1)]

def find(x):
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]

def union(x,y):
    fx,fy = find(x),find(y)
    if fx != fy:
        f[fy] = fx


ans = 0
cnt = 0
edge.sort(key=lambda x:x[2])
for i in edge:
    u,v,w = i
    if find(u) != find(v) and cnt <= n - 1:
        ans += w
        union(u,v)
        cnt += 1
if cnt < n - 1:
    print(-1)
else:
    print(ans)