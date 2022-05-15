
n,m = map(int,input().split())

g = []
for _ in range(n):
    g.append([int(x) for x in input()])

f = [(1,0),(-1,0),(0,1),(0,-1)] # 上下左右

visit = [[0]*m for _ in range(n)]
temp = [[float('inf')]*m for _ in range(n)]
res = float('inf')
# dfs x,y是起点，t是已经经过了2，s是已有最少的经过2的次数
def dfs(x,y,t,s):
    if x == n-1 and y == m-1:
        global res
        res = min(res,s)
        return 

    if s < temp[x][y]:
        temp[x][y] = s
    else:
        return
    for tx,ty in f:
        dx,dy = tx+x,ty+y
        if 0<= dx < n and 0<= dy < m and visit[dx][dy]==0:
            if g[dx][dy] == 2:
                if t == 1: continue
                visit[dx][dy] = 1
                dfs(dx,dy,1,s + 1)
                visit[dx][dy] = 0
            else:
                visit[dx][dy] = 1
                dfs(dx,dy,0,s)
                visit[dx][dy] = 0

visit[0][0] = 1
dfs(0,0,0,0)
if res == float('inf'):
    print(-1)
else:
    print(res)
