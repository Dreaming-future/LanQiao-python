"""
https://www.lanqiao.cn/problems/1317/learning/
难度: 简单   标签: exgcd
"""
from math import gcd

# 扩展欧几里得算法
def exgcd(a,b):
    if b == 0:
        return 1,0,a
    x,y,q = exgcd(b,a%b)
    x,y = y,x-(a//b)*y
    return x,y,q # q就是gcd(a,b)

x,y,m,n,l = map(int,input().split())
a,c = m-n, y-x

if a < 0:
    a = -a
    c = -c

x0,y0,q = exgcd(a,l)

t = (c+l)%l
if t % q:
    print('impossible')
else:
    x0 = x0 * t//q
    b = l//q
    print((x0%b+b)%b)
