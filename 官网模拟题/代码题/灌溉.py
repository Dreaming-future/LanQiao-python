# https://www.lanqiao.cn/problems/551/learning/

n,m = map(int,input().split())
t = int(input())

import collections
pipe = collections.deque()
for i in range(t):
    pipe.append(list(map(int,input().split())))
k = int(input())

mat = [[0]*(m+1) for i in range(n+1)]

for r,c in pipe:
    mat[r][c] = 1

cnt = t
dx = [0,0,1,-1]
dy = [1,-1,0,0]
while k - 1 >= 0:
    k -= 1
    x = len(pipe)
    while x > 0:
        p = pipe.popleft()
        pr,pc = p
        for i in range(4):
            px = pr + dx[i]
            py = pc + dy[i]
            if 0 < px <= n and 0 < py <= m and mat[px][py] == 0:
                mat[px][py] = 1
                cnt += 1
                pipe.append((px,py))
        x -= 1
print(cnt)    