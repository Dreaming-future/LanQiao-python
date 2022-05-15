import os
import sys

# 请在此输入您的代码

n = int(input())
a = list(map(int,input().split()))
a = [0] + a
dp = [0]*(n+1)

for i in range(1,n+1):
  dp[i] = 1

  for j in range(1,i):
    if a[j] < a[i] and dp[i] < dp[j] + 1:
      dp[i] = dp[j] + 1
print(max(dp))