# https://www.lanqiao.cn/problems/1019/learning/


from collections import deque

q = deque([(0,0),(2020,11),(11,14),(2000,2000)])
f = [(1,0),(-1,0),(0,1),(0,-1)]

ans = 4
t = 2020
s = set()
for x,y in q:
    s.add((x,y))
i = 0
while i < t:
    length = len(q)
    j = 0
    while j < length:
        x,y = q.popleft()
        for nx,ny in f:
            nx = x + nx
            ny = y + ny
            if (nx,ny) not in s:
                ans += 1
                s.add((nx,ny))
                q.append((nx,ny))           
        j += 1
    i += 1

print(ans)