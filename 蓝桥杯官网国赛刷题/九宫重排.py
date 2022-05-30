import os
import sys

s = list(input())
e = list(input())

#返回下一个状态中”.“的位置
def f(i):
    if i==0:return [1,3]
    elif i==1:return [0,2,4]
    elif i==2:return [1,5]
    elif i==3:return [0,4,6]
    elif i==4:return [1,3,5,7]
    elif i==5:return [2,4,8]
    elif i==6:return [3,7]
    elif i==7:return [4,6,8]
    else: return [5,7]

from collections import deque
def bfs(start):
    q = deque()
    q.append((start,0))
    path = set()
    path.add("".join(start))
    while q:
        t,ans = q.popleft()
        if t == e:
            print(ans)
            break
        zero = s.index('.')
        next_pos = f(zero)
        for i in next_pos:
            T = t[:]
            T[zero],T[i] = T[i],T[zero]
            st = "".join(T)
            if st not in path:
                q.append((T,ans+1))
                path.add(st)
    else:
        print(-1)
bfs(s)