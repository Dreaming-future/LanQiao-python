# https://www.lanqiao.cn/problems/1174/learning/
# 难度: 简单   标签: dp, 背包, 01背包
import os
import sys


# 请在此输入您的代码
N,V = map(int,input().split())
# f[N][V]
# f[i][j] 代表 i 件物品 ， 容量为 j 的时候，得到最大的价值
f = [[0]*(V+1) for _ in range(N+1)]

for i in range(1,N+1):
    # v为体积， w为价值
    v, w = map(int, input().split())
    for j in range(1,V+1):
        # 第i件物品有两种选择，
        # 第1种是选第i件物品，f[i-1][j]
        # 第2种是不选第i件物品，f[i-1][j]
        if j < v: 
            f[i][j] = f[i-1][j]
        else:
            f[i][j] = max(f[i-1][j], f[i-1][j-v] + w)

print(f[N][V])