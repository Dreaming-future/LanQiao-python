# https://www.lanqiao.cn/problems/553/learning/
n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

dp = [[-10000]*m for _ in range(n)]
dp[0][0] = mat[0][0]

for i in range(n):
    for j in range(m):
        if i+1 <= n-1:
            dp[i+1][j] = max(dp[i+1][j],mat[i+1][j]+dp[i][j])
        if i+2 <= n-1:
            dp[i+2][j] = max(dp[i+2][j],mat[i+2][j]+dp[i][j])
        if i+3 <= n-1:
            dp[i+3][j] = max(dp[i+3][j],mat[i+3][j]+dp[i][j])
        if j+1 <= m-1:
            dp[i][j+1] = max(dp[i][j+1],mat[i][j+1]+dp[i][j])
        if j+2 <= m-1:
            dp[i][j+2] = max(dp[i][j+2],mat[i][j+2]+dp[i][j])
        if j+3 <= m-1:
            dp[i][j+3] = max(dp[i][j+3],mat[i][j+3]+dp[i][j])
        if i+1 <= n-1 and j+1 <= m-1:
            dp[i+1][j+1] = max(dp[i+1][j+1],mat[i+1][j+1]+dp[i][j])
        if i+1 <= n-1 and j+2 <= m-1:
            dp[i+1][j+2] = max(dp[i+1][j+2],mat[i+1][j+2]+dp[i][j])
        if i+2 <= n-1 and j+1 <= m-1:
            dp[i+2][j+1] = max(dp[i+2][j+1],mat[i+2][j+1]+dp[i][j])
print(dp[-1][-1])