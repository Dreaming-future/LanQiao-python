import os
import sys

dp = [[0]*6000 for _ in range(6000)]

def dist(a,b):
    lena = len(a)
    lenb = len(b)
    # dp[i][j]为a从0~i b从0～j 的字符串
    for i in range(lena):
        dp[i][0] = i
    for j in range(lenb):
        dp[0][j] = i
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                # 如果相等，那就跟之前一样
                dp[i][j] = dp[i-1][j-1]
            else:
                # 漏，错，重 一共三种情况
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1

    return dp[lena-1][lenb-1]

n = int(input())
for _ in range(n):
    a = input()
    b = input()
    res = dist(a,b)
    print(res)