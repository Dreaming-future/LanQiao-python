import os
import sys

s = []
hole = [0]*7
for i in range(6):
    # 每件装备 以及装备孔的级别
    s.append(list(map(int,input().split())))
    for j in range(1,7):
        # count(j)是计算各个等级的个数
        hole[j] += s[i][1:].count(j)

# 输入装饰珠，n个装饰珠
n = int(input())
w = [0]
for i in range(n):
    # 每个装饰珠，镶嵌的价值
    # w[i][0] 为等级 w[1] 为装饰珠最大个数 w[i][2:] 装饰珠对于个数的价值
    w.append(list(map(int,input().split())))


# 用hole[j]记录6件装备共有j级孔hole[j]个
# print(hole)

# total总共的孔
total = sum(hole)

# dp[i][j]表示前 i 种珠子放入 j 个孔中所能产生的最大价值
dp = [[0]*(total+1) for _ in range(n+1)]

kind = 0
ans = 0
# level 表示装饰珠的等级
for level in range(4,0,-1):
    # 该等级开发的孔数
    ans += hole[level]
    if ans == 0: continue # 没有孔数，直接退出
    # 第k种珠子
    for k in range(1,n+1):
        # w[k][0] 为等级
        if w[k][0] == level:
            kind += 1
            # 必须先平行转移，因为有好几种转移情况(放i个)
            for i in range(1,ans+1):
                dp[kind][i] = dp[kind-1][i]
            # 放i个该种珠子
            for i in range(1,w[k][1]+1):
                for j in range(ans,i-1,-1):
                    dp[kind][j] = max(dp[kind][j],dp[kind-1][j-i]+w[k][i+1])
            
print(max(dp[kind]))  