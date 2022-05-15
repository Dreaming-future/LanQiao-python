import os
import sys
import math
# 请在此输入您的代码

dp = [0]*10000
dp[0] = 1

n = int(input())
for i in range(n):
    a = int(input())
    if i == 0:
        g = a
    else:
        g = math.gcd(a,g)
    for j in range(1,10000):
        # 完全背包问题
        if j >= a and dp[j - a] == 1:
            dp[j] = 1

if g == 1:
    print(dp.count(0))
else:
    print('INF')