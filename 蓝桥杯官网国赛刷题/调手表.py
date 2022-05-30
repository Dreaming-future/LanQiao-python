import os
import sys

# 请在此输入您的代码
n,k = map(int,input().split())

dp = [i for i in range(n)]

MAX = 0
for i in range(k):
    t = i*k%n
    dp[t] = min(dp[t],i)

for j in range(n):
    dp[j] = min(dp[j-1]%n+1,dp[(j-k)%n]+1,dp[j])
print(max(dp))