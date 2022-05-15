# https://www.lanqiao.cn/problems/1276/learning/
# 难度: 简单   标签: 差分

n,q = map(int,input().split())
a = [0]+list(map(int,input().split()))

b = [0]*(n+2)
for i in range(1,n+1):
    b[i] = a[i] - a[i-1]
    
for i in range(q):
    l,r,x = map(int,input().split())
    b[l] += x
    b[r+1] -= x

for i in range(1,n+1):
    a[i] = b[i] + a[i-1]
    if a[i] <= 0:
        print(0,end =' ')
    else:
        print(a[i],end = ' ')