'''
https://www.lanqiao.cn/problems/1320/learning/
难度: 简单   标签: 期望DP
'''

import os
import sys

# 请在此输入您的代码
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0]*(n+1) #dp[i]表示扔到第i面还需要扔的次数
    for i in range(n-1,-1,-1):
        dp[i] = dp[i+1] + n/(n-i)
    print('%.2f'%dp[0])
