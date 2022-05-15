# https://www.lanqiao.cn/problems/1216/learning/
# 难度: 简单   标签: bfs

from re import A

from collections import deque
n,m = map(int,input().split())
G = [[]]
for _ in range(n):
    G.append([0] + list(map(int,input().split())))

x1, y1, x2, y2 = map(int,input().split())

f = [(0,-1),(0,1),(1,0),(-1,0)] # 方向
ans = float('inf')
def bfs(x,y):
    q = deque()
    vis = [[0]*(m+1) for _ in range(n+1)]
    q.append((x,y,0))
    while q:
        a,b,step = q.popleft()
        if a == x2 and b == y2:
            return step
        vis[a][b] = 1
        for X,Y in f:
            X, Y = a + X, b + Y
            if 1 <= X <= n and 1<= Y <= m:
                if G[X][Y] == 1 and not vis[X][Y] and 1 <= X <= n and 1<= Y <= m:
                    q.append((X,Y,step+1))
                    vis[X][Y] = 1
    return -1

ans = bfs(x1,y1)
print(ans)
