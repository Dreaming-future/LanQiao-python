'''
https://www.lanqiao.cn/problems/1233/learning/
难度: 简单   标签: 区间DP
'''

import os
import sys

# 请在此输入您的代码
n = int(input())
stone = list(map(int,input().split()))

ans = [0]*(n+1) # 作为一个前缀和数组
for i in range(n):
    ans[i+1] = ans[i] + stone[i]

dp = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

# 首先枚举长度
for l in range(2,n+1):
    # 然后枚举起点
    for i in range(n):
        ends = i + l - 1
        if ends >= n:
            break
        # 然后枚举分割点
        for k in range(i,ends):
            dp[i][ends] = min(dp[i][ends],dp[i][k]+dp[k+1][ends] + ans[ends+1]-ans[i])

print(dp[0][n-1])