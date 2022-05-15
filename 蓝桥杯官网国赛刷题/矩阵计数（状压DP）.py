# https://www.lanqiao.cn/problems/246/learning/

import os
import sys

n,m = map(int,input().split())
L = 1<<m
def judge(x):
  c = 0
  for _ in range(L):
    if x&1 == 0:
      c = 0
    else:
      c += 1
    if c == 3:
      return False

    x >>= 1
  return True

row = []
for i in range(L):
  if judge(i):
    row.append(i)

# dp[i][j][k]，表示第i行的合法状态时j,它前一行的合法状态是k时，符合状态的矩阵有多少个
# dp = [[[0]*L for _ in range(L)] for _ in range(n)]
dp = [[] for _ in range(n)]
for i in range(n):
  dp[i] = [[0]*L for _ in range(L)]

l = len(row)
for i in range(l):
  dp[0][row[i]][0] = 1

# 枚举前i行
for i in range(1,n):
  for j in range(l):
    for k in range(l):
      for p in range(l):
        if row[j] & row[k] & row[p] == 0:
          dp[i][row[j]][row[k]] += dp[i-1][row[k]][row[p]]
ans = 0
for i in range(l):
  for j in range(l):
    ans += dp[-1][row[i]][row[j]]
print(ans)