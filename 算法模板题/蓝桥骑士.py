'''
https://www.lanqiao.cn/problems/1188/learning/
难度: 中等   标签: dp, LIS
'''

import os
import sys
import bisect
# 请在此输入您的代码

n = int(input())
a = list(map(int,input().split()))

dp = [float('inf')]*(n+1)
dp[0] = a[0]
for i in range(1,n):
    t = bisect.bisect_left(dp,a[i])
    dp[t] = a[i]

print(bisect.bisect_left(dp,float('inf')))