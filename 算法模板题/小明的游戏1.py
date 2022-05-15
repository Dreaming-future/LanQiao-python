'''
https://www.lanqiao.cn/problems/1218/learning/
难度: 简单   标签: nim博弈
'''

import os
import sys

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    a = list(map(int, input().split()))
    for i in range(n):
        ans ^= a[i]
    if ans!=0:
       print('NO')
    else:
       print('YES')