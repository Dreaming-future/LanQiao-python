# https://www.lanqiao.cn/problems/186/learning/
# 状压DP

n,m,k = map(int,input().split())
dp = [float('inf')]*(1<<m)
s = [0]*n
for i in range(n):
    candies = list(map(int,input().split()))
    state = 0 # 糖果的状态
    for candy in candies:
        candy -= 1 # 从0开始
        state = state | (1<<candy) 
    s[i] = state # 记录标记
    dp[state] = 1 # 记录状态，这样的糖果需要一包即可
    
goal = (1<<m) - 1
for i in range(n):
    for j in range(goal+1):
        if dp[j] == -1: continue # 这个状态没有买到糖果，直接进行跳过
        dp[j|s[i]] = min(dp[j|s[i]],dp[j]+1) # 状态转移 

if dp[goal] != float('inf'):
    print(dp[goal])
else:
    print(-1)