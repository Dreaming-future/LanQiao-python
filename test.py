

from dis import dis
from tkinter import N


def floyd(dist):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[i][j] = max(dist[i][k] + dist[k][j],dist[i][j])
            
            
def djs(s):
    vis = [False]*N
    dist = [float('inf')]*N
    dist[s-1] = 0
    for i in range(n):
        x = -1
        for y,u in enumerate(vis):
            if not u and (x==-1 or dist[y] < dist[x]):
                x = y
        vis[x] = 1
        for y,w in enumerate(graph[x]):
            dist[y] = min(dist[y],dist[x]+w)
            
            