
import os
import sys
N = 7
path = [[False for _ in range(8)]for _ in range(8)]
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    global result
    path[x][y] = True
    if x == 0 or y == 7:
        result += 1
        return
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx<0 or xx>7 or yy <0 or yy>7: continue
        if path[xx][yy] or xx == yy: continue
        path[xx][yy] = True
        dfs(xx, yy)
        path[xx][yy] = False


for i in range(1,N):
    path[i][i] = True
    dfs(i,i)
    path[i][i] = False
print(result+2)