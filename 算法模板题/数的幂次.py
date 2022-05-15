'''
https://www.lanqiao.cn/problems/1181/learning/
难度: 简单   标签: 快速幂
'''

import os
import sys

# 请在此输入您的代码

def quickpow(n,m,p):
    res = 1
    while m:
        if m & 1:
            res = (res * n)%p
        n = (n*n)%p
        m = m>>1
    return res

t = int(input())
for i in range(t):
    n, m, p = map(int,input().split())
    print(quickpow(n,m,p))