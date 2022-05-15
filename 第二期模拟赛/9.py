
n = int(input())
MOD = 1000000007

import math
print(math.comb(n,n//2)%MOD)


dp = [0]*1001
for i in range(1,n+1):
    dp[0] = 1
    dp[i] = 1
    for j in range(i-1,0,-1):
        dp[j] = (dp[j]+dp[j-1])%MOD
print(dp[n//2])
