
# http://118.190.20.162/view.page?gpid=T120

# 记录到达的边 和 权值
class Edge():
    def __init__(self,v,w):
        self.v = v
        self.w = w

n,m,k = map(int,input().split())

# 记录每一个酒店对食材的需要情况
request = [0]*(n+1)
for i in range(1,n+1):
    f = list(map(int,input().split()))
    for j in range(k):
        if f[j] == 1:
            request[i] |= (1<<j) # 位运算的思想


from collections import defaultdict
from re import L
import turtle
# 建立图
graph = defaultdict(list)
for i in range(n-1):
    u,v,w = map(int,input().split())
    # 记录边权
    graph[u].append(Edge(v,w))
    graph[v].append(Edge(u,w))

# u是出发点，src是上一个点
def dfs(u, src):
    mx = 0 
    # 遍历所有u为顶点的路径
    for i in range(len(graph[u])):
        v = graph[u][i].v
        w = graph[u][i].w
        if v == src:
            # 与来源相同，跳过
            continue
        re = dfs(v,u)
        # 这个节点对食材有要求
        if flag[v]:
            # 为了达到v，一定会经过u，所以需要进行标记
            flag[u] = 1
            global roadTime
            roadTime += w # 路径加了w的时间
            # 判断是否是最长等待时间
            mx = max(mx, re + w)
    # 返回本顶点出发的最长时间
    return mx
            
# 计算从第i个酒店出发，到达第j个食材的最大等待时间，并且记录进二维数组中
maxWaitTimes = [[0]*k for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(k):
        flag = [0]*(n+1)
        for ii in range(n+1):
            if (request[ii] >> j)&1: flag[ii] = 1
        # 配送所有酒店所需要的单程时间
        roadTime = 0
        # 从第i个酒店出发的最大时间
        mx = dfs(i,-1)
        # 最好情况就是，其他路径来回两次，最长路径只经过一次
        maxWaitTimes[i][j] = 2*roadTime - mx

# if m == k:
#     ans = 0
#     for j in range(k):
#         food_min = float('inf')
#         for i in range(1,n+1):
#             food_min = min(maxWaitTimes[i][j],food_min)
#         ans = max(food_min,ans)
#     print(ans)
# else:
def judge(mid):
    dp = [[0]*(1<<k) for _ in range(m+1)]
    T = [0]*(n+1) # 记录每一个节点在满足mid的条件下可以运输食材的情况
    # 遍历酒店
    for i in range(1,n+1):
        # 遍历食材
        for j in range(k):
            # 该酒店配送该食物时间小于mid，酒店i可以用于配送食材j
            if maxWaitTimes[i][j] <= mid:
                T[i] |= (1<<j)
    dp[0][0] = 1
    tmp = [[0]*(1<<k) for _ in range(m+1)]
    tmp[0][0] = 1
    # 遍历酒店i，以i为出发点，查看食材配送情况
    for i in range(1,n+1):
        # 遍历检查点，加入i在第j个检查点的情况
        for j in range(1,m+1):
            tmp = dp[:]
            for ii in range(k<<1):
                dp[j][ii] |= tmp[j][ii]
                # 转移方程，第j个检查点对每个食材的配送情况 = 第j-1个检查点食材配送情况 + 酒店i的食材配送情况
                dp[j][ii | T[i]] |= tmp[j-1][ii]
    # 判断是否所有食材配送到达
    return dp[m][(1<<k)-1]
l,r = 1,int(1e9)
ans = 0
while l <= r:
    mid = (l+r)>>1
    if judge(mid):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1
print(ans)


