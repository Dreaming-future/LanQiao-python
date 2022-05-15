
# DP

s=[i*i for i in range(1,int(2019**0.5)+1)]
x=2019
dp=[0]*(x+1)

dp[0]=1
for i in s:
  for j in range(x,i-1,-1):
    dp[j] +=dp[j-i]
print(dp[x])