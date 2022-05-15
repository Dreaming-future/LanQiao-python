'''
https://www.lanqiao.cn/problems/1221/learning/
难度: 简单   标签: 三分
'''

import os
import sys

# 请在此输入您的代码

a,b,c,q = map(int,input().split())

def f(x):
    return a*x*x + b*x + c

for _ in range(q):
    l,r = map(int,input().split())
    x = -b/(2*a)
    if a > 0:
        if l >= x:
            res = f(r)
        elif r<=x:
            res = f(l)
        else:
            res = max(f(l),f(r))
    elif a < 0:
        if l >= x:
            res = f(l)
        elif r<=x:
            res = f(r)
        else:
            res = f(int(x))
    elif a == 0:
        if b >= 0:
            res = f(r)
        else:
            res = f(l)
    print('%.2f'%res)