'''
https://www.lanqiao.cn/problems/1260/learning/
难度: 简单   标签: GCD
'''

import os
import sys

# 请在此输入您的代码

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    print('%d'%gcd(a,b))