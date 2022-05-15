'''
https://www.lanqiao.cn/problems/1121/learning/
难度: 简单   标签: Floyd
'''

n,m,q = map(int,input().split())

MAP = [[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(m):
    u,v,w = map(int,input().split())
    MAP[u][v] = w


def floyd(MAP):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if MAP[i][j] > MAP[i][k] + MAP[k][j]:
                    MAP[i][j] = MAP[i][k] + MAP[k][j]

floyd(MAP)
for _ in range(q):
    st,ed = map(int,input().split())
    res = MAP[st][ed]
    if res != float('inf'):
        print(res)
    else:
        print(-1)