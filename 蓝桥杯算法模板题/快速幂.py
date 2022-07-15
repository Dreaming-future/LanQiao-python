

def qpow(x,n):
    res = 1
    while n:
        if n&1:
            res = res*x
        x = x*x
        n >>= 1 
    return res

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

def qpow_matrix(x,n):
    m = len(x)
    res = [[0]*m for _ in range(m)]
    for i in range(m): res[i][i] = 1
    while n:
        if n&1:
            res = multi(res,x)
        x = multi(x,x)
        n >>= 1
    return res