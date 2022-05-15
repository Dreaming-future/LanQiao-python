"""
https://www.lanqiao.cn/problems/1180/learning
难度: 简单   标签: 矩阵快速幂
"""

def multi(x,y):
    n,m,k = len(x),len(x[0]),len(y[0])
    res = [[0]*k for _ in range(n)]
    res = [[0,0],[0,0]]
    for i in range(n):
        for j in range(k):
            ans = 0
            for w in range(m):
                ans += x[i][w] * y[w][j]
            res[i][j] = ans
    return res

def quickpow(x,n):
    res= [[1,0],[0,1]]
    while n:
        if n & 1:
            res = multi(res,x)
        x = multi(x,x)
        n = n>>1

    return res

q = [[1,1],[1,0]]
t = int(input())
for _ in range(t):
    n = int(input())
    res = quickpow(q,n-1)
    print(res[0][0])
