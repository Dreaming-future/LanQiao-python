'''
https://www.lanqiao.cn/problems/1368/learning/
难度: 简单   标签: 二阶差分
'''

import os
import sys



# 二维差分
n,m = map(int,input().split())
a = [0]*(n+2)
b = [0]*(n+2)
c = [0]*(n+2)
for _ in range(m):
    l,r,s,e = map(int,input().split())
    d = (e - s)//(r-l)
    c[l] += s
    c[l+1] += d - s
    c[r+1] -= d + e 
    c[r+2] += e

res = 0
for i in range(1,n):
    b[i] = b[i-1] + c[i] # c[i] = b[i] - b[i-1]
    a[i] = a[i-1] + b[i] # b[i] = a[i] - a[i-1]
    res += a[i]
print(res)