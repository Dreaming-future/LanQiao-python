'''
https://www.lanqiao.cn/problems/1189/learning/
难度: 简单   标签: dp, LCS
'''

import os
import sys

# 请在此输入您的代码

n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))
b = [0] + list(map(int,input().split()))


# 取最大的长度
x = max(n,m) + 1

# dp[i][j]代表的就是a数组a[:i] 和 b[:j] 的最长公共子序列长度
dp = [[0]*x for _ in range(x)]


for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i] != b[j]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j] = dp[i-1][j-1] + 1 # 当前数字相同，所以为d[i-1][j-1] + 1
print(dp[n][m])
