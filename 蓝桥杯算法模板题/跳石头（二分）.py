# https://www.lanqiao.cn/problems/364/learning/
import os
import sys

# 请在此输入您的代码

L, N , M = map(int,input().split())
d  = []
for i in range(N):
  d.append(int(input()))

def check(x):
  num = 0
  pos = 0
  for i in range(N): 
    if d[i] - pos < x: # remove i stone
      num += 1
    else:
      pos = d[i]
  return num <= M


l,r = 1,L
while l < r:
  mid = (l + r) >> 1
  if check(mid):
    l = mid + 1
  else:
    r = mid
if check(l):
  print(l)
else:
  print(l-1)