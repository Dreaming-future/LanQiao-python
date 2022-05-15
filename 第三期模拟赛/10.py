n,k = map(int,input().split())
a = list(map(int,input().split()))
s = input()

ans = 0
# cnt 代表s中下标的个数，idx是从这部分可以深度搜索
# length是长度
def dfs(cnt,idx,length):
    global ans
    if s[idx] == '1': # 如果遇到1 
        cnt += 1
    length += 1
    if idx == n-1 and cnt >= k:
        ans = max(ans,length)
    
    for i in range(idx+1,n):
        if a[i] > a[idx]:
            dfs(cnt,i,length)

for i in range(n):
    dfs(0,i,0)
print(ans)
# dp[i][j]表示取i个数中，至少有j个数在s下标下的长度
dp = [[-1]*(k+1) for _ in range(n+1)]

dp[0][0] = 1

if s[0] == '1':
    dp[0][1] = 1

for i in range(1,n):
    dp[i][0] = 1 # 单独一个i最少可以
    for j in range(k): # 去s中的数
        # a[i]为下标数
        if s[i] == '1' and j > 0:
            flag = True
        else:
            flag = False
            
        for x in range(1,i):
            # 从前面寻找最大的序列
            if a[x] > a[j]: continue
            # a[i] 在s中
            if flag:
                if dp[x][j-1] == -1:
                    continue
                dp[i][j] = max(dp[i][j],dp[x][j-1] + 1)
            else:
                if dp[x][j] == -1:
                    continue
                dp[i][j] = max(dp[i][j],dp[x][j] + 1) 
print(dp[n-1][k])

