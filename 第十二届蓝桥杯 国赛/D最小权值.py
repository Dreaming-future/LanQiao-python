

dp = [float('inf')]*2022
dp[0] = 0

for i in range(1,2022):
    for j in range(i): # 枚举左子树的节点数
        dp[i] = min(dp[i],1+2*dp[j]+3*dp[i-j-1]+j*j*(i-j-1)) # 动态转移方程

print(dp[2021]) # 2653631372