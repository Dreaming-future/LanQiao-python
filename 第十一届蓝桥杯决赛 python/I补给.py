# import functools
  
# def distance(loc1, loc2):
#     return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5
 
# # 迪杰特斯拉算法
# @functools.lru_cache()
# def djs(start, goal):
#     if goal == start: return 0
#     close = [[graph[start][i], start] for i in range(n)]
#     visited = [0] * n
#     visited[start] = 1
#     # 剩下有n-1个点
#     for _ in range(n - 1):
#         closest = INF
#         for i in range(n):
#             if not visited[i] and close[i][0] < closest:
#                 closest = close[i][0]
#                 nextvisit = i
#                 pre = close[i][1]
#         # 找到下一个点
#         if nextvisit == goal:
#             return closest
#         visited[nextvisit] = 1
#         for i in range(n): 
#             # 如果通过i能够更快，则更新最短距离
#             if not visited[i] and graph[nextvisit][i] + closest < close[i][0]:
#                 close[i][0] = graph[nextvisit][i] + closest
#                 close[i][1] = nextvisit
 
 
# n, D = map(int, input().split())
# location = []
# for i in range(n):
#     x, y = map(int, input().split())
#     location.append((x, y))
# INF = float('inf')
# graph = [[INF] * n for i in range(n)]
 
# for u in range(n):
#     for v in range(u + 1, n):
#         dis = distance(location[u], location[v])
#         if dis <= D:
#             graph[u][v] = graph[v][u] = dis
 
# # 状态压缩dp
# # dp[i][j]为从i出发完成j状态的游历后回到0的最短路径长度
# dp = [[0] * (1 << n) for i in range(n)]
# for i in range(n):
#     dp[i][0] = djs(i, 0)
# for state in range(1, 1 << n):
#     for i in range(n):
#         M = INF
#         for j in range(n):
#             if 1 << j & state != 0:
#                 sub = state ^ 1 << j
#                 M = min(M, djs(i, j) + dp[j][sub])
#         dp[i][state] = M
 
# print('%.2f'%dp[0][(1 << n) - 1])

def distance(loc1, loc2):
    return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5
n, D = map(int, input().split())
location = []
for i in range(n):
    x, y = map(int, input().split())
    location.append((x, y))
    
INF = float('inf')
graph = [[0] * n for i in range(n)]
 
for u in range(n):
    for v in range(u + 1, n):
        dis = distance(location[u], location[v])
        graph[u][v] = graph[v][u] = dis
        if dis > D:
            graph[u][v] = graph[v][u] = INF

# Flody算法
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

# 状态压缩dp
# dp[i][j]为从i出发完成j状态的游历后回到0的最短路径长度
dp = [[INF] * n for i in range(1<<n)]
dp[1][0] = 0

for i in range(1<<n):
    for j in range(n):
        if i>>j & 1:
            for k in range(n):
                if (i - (1 << j)) >> k & 1:
                    dp[i][j] = min(dp[i][j],dp[i - (1<<j)][k] + graph[k][j])

ans = INF
for i in range(1,n):
    ans = min(ans, dp[(1<<n) - 1][i] + graph[i][0])
print('%.2f'%ans)