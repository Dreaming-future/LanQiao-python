import os
import sys
sys.setrecursionlimit(1000000000)
# 请在此输入您的代码
n = int(input())
nums = list(map(int,input().split()))

import collections
s = collections.defaultdict(list)
for i in range(n-1):
  a,b = list(map(int,input().split()))
  s[a].append(b)
  s[b].append(a)

# print(s)
ans = 0
vis = [0]*n
dp = [[0]*2 for _ in range(n)]
# 树形DP
def dfs(i):
  # 选择了 当前节点 值为nums[i]
  dp[i][1] = nums[i]
  dp[i][0] = 0
  vis[i] = 1
  # 得到相连的点
  for num in s[i+1]:
    # 如果节点未访问过
    num = num - 1
    if vis[num] == 0:
      # 对节点进行一个dfs
      dfs(num)
      # 选择当前节点的dp是，是否选择孩子节点
      dp[i][1] += max(dp[num][0],dp[num][1])
    else:
      # 已经选择了节点
      dp[i][1] = max(dp[i][1],nums[i])
      dp[i][0] = max(dp[i][0],0)  
      
dfs(0)
# print(dp)
ans = 0
for i in range(n):
  ans = max(ans,dp[i][1])
  ans = max(ans,dp[i][0])
print(ans)