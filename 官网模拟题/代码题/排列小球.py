# https://www.lanqiao.cn/problems/546/learning/

r,g,b = map(int,input().split())

cnt = 0
# 状态x,y,z代表的是剩下三种球的数量，strlen代表当前最大序列的长度，color代表最大序列的颜色
def dfs(x,y,z,strlen,color):
    if x == 0 and y == 0 and z == 0: # 剩下的球没了，说明已经排完了
        global cnt
        cnt += 1
        return
    if color != 0:
        for i in range(strlen+1,x+1):
            dfs(x-i,y,z,i,0)
    if color != 1:
        for i in range(strlen+1,y+1):
            dfs(x,y-i,z,i,1)
    if color != 2:
        for i in range(strlen+1,z+1):
            dfs(x,y,z-i,i,2)

dfs(r,g,b,0,0)
dfs(r,g,b,0,1)
dfs(r,g,b,0,2)
print(cnt//2)