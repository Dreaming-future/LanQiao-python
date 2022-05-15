MOD = 998244353
n = int(input())

ans = 2 
dp = [0]*(n+3)
dp[1] = 0
dp[2] = 1
for i in range(3,n+1):
    dp[i] = (dp[i-1]*i + ans*i*(i-1)//2)%MOD
    ans = (ans*i)%MOD # 计算全排列数

print(dp[n]%MOD)
