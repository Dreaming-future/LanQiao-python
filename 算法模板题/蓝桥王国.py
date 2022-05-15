'''
https://www.lanqiao.cn/problems/1122/learning/
难度: 简单   标签: Dijkstra
'''

import os
import sys
import functools

n,m = map(int,input().split())
INF = float('inf')
graph = [[INF] * (n) for _ in range(n)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u-1][v-1] = w 

def djs(start):
    visited = [0]*n
    dist = [INF]*n
    dist[start - 1] = 0

    for i in range(n):
        # 找到未标记最近的点
        x = -1
        for y,u in enumerate(visited):
            if not u and (x == -1 or dist[x] > dist[y]):
                x = y
        visited[x] = 1
        for y,w in enumerate(graph[x]):
            dist[y] = min(dist[y],dist[x] + w)

    print(" ".join(map(str,dist)))

djs(1)