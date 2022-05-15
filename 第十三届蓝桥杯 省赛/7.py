MOD = 998244353
n = int(input())

dp = [0]*(n+3)


dp[1] = 0
dp[2] = 1

ans = 2
##for i in range(3,n+1):
##    for j in range(i):
####        print(dp[i-1],j*ans)
##        dp[i] += (j*ans + dp[i-1])%MOD
##    ans = (ans*i)%MOD

for i in range(3,n+1):
    j = i-1
    dp[i] = (dp[i-1]*i + ans*j*(j+1)//2)%MOD
    ans = (ans*i)%MOD

print(dp[n]%MOD)
