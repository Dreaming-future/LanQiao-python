
"""
https://www.lanqiao.cn/problems/1179/learning/
难度: 中等   标签: dp, 背包, 树形背包
"""
import sys
sys.setrecursionlimit(1<<31-1)
N,V = map(int,input().split())

# 存储对应的依赖
f = [[0] for _ in range(N+1)]
v,w = [0],[0]

for i in range(1,N+1):
    vi,wi,si = map(int,input().split())
    if si == 0:
        root = i
    else:
        f[si].append(i)
    v.append(vi)
    w.append(wi)

dp = [[0]*(V+1) for _ in range(N+1)]

# 两个参数，分别是物品和体积
def dfs(u):
    # 计算物品依赖
    for i in range(1,len(f[u])):
        son = f[u][i]
        dfs(son)
        for j in range(V-v[u],-1,-1):  # 遍历体积
            for k in range(j+1):
                dp[u][j] =  max(dp[u][j],dp[u][j-k] + dp[son][k])
    for i in range(V,v[u]-1,-1):
        dp[u][i] = dp[u][i-v[u]] + w[u]
    for i in range(v[u]):
        dp[u][i] = 0

dfs(root)
print(dp[root][V])