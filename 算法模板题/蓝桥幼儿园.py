'''
https://www.lanqiao.cn/problems/1135/learning/
难度: 简单   标签: 并查集
'''

N,M = map(int,input().split())
f = [i for i in range(N+1)]
def find(x):
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]

def union(x,y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        f[fy] = fx
        
for i in range(M):
    op,x,y = map(int,input().split())
    if op == 2:
        if find(f[x]) == find(f[y]):
            print('YES')
        else:
            print('NO')
    elif op == 1:
        union(x,y)