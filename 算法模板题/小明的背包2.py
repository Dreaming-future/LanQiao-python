'''
https://www.lanqiao.cn/problems/1175/learning/
难度: 简单   标签: DP, 背包, 完全背包
'''

import os
import sys

# 请在此输入您的代码
N,V = map(int,input().split())

# f[i][j]表示前i种，总体积不超过j，最大的总价值
f = [[0]*(V+1) for _ in range(N+1)]


# 完全背包问题，可以买多个
for i in range(1,N+1):
    v,w = map(int,input().split())
    for j in range(1,V+1): # 这里是体积的范围
        # t = j//v
        # f[i][j] = f[i-1][j]
        # for x in range(1,t+1): # x是第i件物品的数量
        #     f[i][j] = max(f[i][j],f[i-1][j-x*v]+w*x)
        # 优化后写法，已经把所有的也考虑进去了
        if j < v:
            f[i][j] = f[i-1][j] # 相当于不买第 i 件物品
        else:
            f[i][j] = max(f[i-1][j],f[i][j-v] + w) # 这里是比较买i件物品和不买i件物品
print(f[N][V])


# 压缩成一维
# dp = [0]*(V+1)
# v,w = [],[]
# for i in range(N):
#     v,w = map(int,input().split())
#     for j in range(1,V+1):
#         if j >= v:
#             dp[j] = max(dp[j-v] + w, dp[j])
# print(dp[V])


