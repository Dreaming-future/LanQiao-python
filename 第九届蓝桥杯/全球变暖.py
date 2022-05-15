# https://www.lanqiao.cn/problems/178/learning/
import os
import sys

# 请在此输入您的代码
import collections

d = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x,y):
    global flag
    q = collections.deque()
    q.append((x,y))
    vis[x][y] = 1
    while q:
        t = q.popleft()
        tx,ty = t[0],t[1]
        if mp[tx-1][ty] == '#' and mp[tx+1][ty] == '#' and mp[tx][ty+1] == '#' and mp[tx][ty-1] == '#':
            flag = 1
        for i in range(4):
            nx = tx + d[i][0]
            ny = ty + d[i][1]
            if vis[nx][ny] == 0 and mp[nx][ny] == '#':
                q.append((nx,ny))
                vis[nx][ny] = 1
     
n = int(input())
mp = []
for i in range(n):
    mp.append(list(input()))

vis = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if vis[i][j] == 0 and mp[i][j] == '#':
            flag = 0
            bfs(i,j)
            if flag == 0:
                cnt += 1
print(cnt)