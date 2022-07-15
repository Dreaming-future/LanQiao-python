
# http://118.190.20.162/view.page?gpid=T54
# 并查集 + Kruskal算法

n,m = map(int,input().split())

w = []
for i in range(m):
    a,b,c = map(int,input().split())
    w.append((a,b,c))

f = [i for i in range(n+1)]

def get_father(x):
    if f[x] != x:
        f[x] = get_father(f[x])
    return f[x]

def union(x,y):
    fx,fy = get_father(x),get_father(y)
    if fx != fy:
        f[fy] = fx

# 排序
w.sort(key = lambda x:x[2])

# 构建最小生成树0
for i in w:
    u,v,w = i
    if get_father(u) != get_father(v):
        union(u,v)
        if get_father(1) == get_father(n):
            print(w)
            break