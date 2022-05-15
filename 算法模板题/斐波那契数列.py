'''
https://www.lanqiao.cn/problems/1180/learning/
难度: 简单   标签: 矩阵快速幂
'''

# 请在此输入您的代码

def multi(X,Y):
    n,m,k = len(X),len(X[0]),len(Y[0])
    res =[[0]*k for _ in range(n)]
    for i in range(n):
      for j in range(k):
        ans = 0
        for x in range(m):
          ans += X[i][x]*Y[x][j]
        res[i][j] = ans
    return res


def fastpow(X,m):
    res = [[1, 0], [0, 1]]
    while m:
        if m&1:
            res = multi(res,X)
        X = multi(X,X)
        m = m>>1
    return res

t = int(input())
q = [[1,1],[1,0]]
for _ in range(t):
    n = int(input())
    res = fastpow(q,n-1)
    res = res[0][0]
    print(res)
    