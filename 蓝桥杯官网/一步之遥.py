import os
import sys

# 请在此输入您的代码

from collections import deque

f = [97,-127]

s = set()
def bfs():
  q = deque()
  q.append((0,0))
  
  while q:
    cnt,ans = q.popleft()
    if ans == 1:
      return cnt
    for x in f:
      d = ans + x
      if d not in s:
        s.add(d)
        q.append((cnt+1,d))
        
cnt = bfs()
print(cnt)