import sys
import os

n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))

# for i in range(n//2+1,n):
#     for j in range(i+1):
#         if j < i - n//2 or j > n//2:
#             dp[i][j] = -1
            
# for i in range(n-2,-1,-1):
#     for j in range(i+1):
#         dp[i][j] += max(dp[i+1][j+1],dp[i+1][j])
        
# print(dp[0][0])

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += dp[i-1][0]
        elif j == i:
            dp[i][j] += dp[i-1][-1]
        else:
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])
            
if n % 2 == 1:
    print(dp[n-1][n//2])
else:
    print(max(dp[n-1][n//2-1],dp[n-1][n//2]))