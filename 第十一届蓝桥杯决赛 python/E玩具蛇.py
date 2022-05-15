
map = [[0]*4 for i in range(4)]
visit=[[False]*4 for i in range(4)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
ans = 0
def dfs(x,y,step):
    global ans
    if step == 16:
        ans += 1
        return
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < 4 and 0 <= ty < 4 and not visit[tx][ty]:
            visit[tx][ty] = True
            dfs(tx,ty,step+1)
            visit[tx][ty] = False

for i in range(4):
    for j in range(4):
        visit[i][j]=True
        dfs(i,j,1)
        visit[i][j]=False
print(ans)