# https://www.lanqiao.cn/problems/1372/learning/
import os
import sys

# 请在此输入您的代码

n,S = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
pos = 0
res = n + 1
s = 0
while True:
  while pos < n and ans < S: 
      ans += a[pos]
      pos += 1
  if ans < S: break
  res = min(res, pos - s)
  ans -= a[s]
  s += 1
if res!= n + 1:
    print(res)
else:
    print(0)
