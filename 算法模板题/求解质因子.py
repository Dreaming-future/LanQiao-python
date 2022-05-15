'''
https://www.lanqiao.cn/problems/1284/learning/
难度: 简单   标签: 唯一分解定理, 约数定理
'''

import os
import sys

# 请在此输入您的代码
n = int(input())
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        print(i,end=' ')
        while n % i == 0:
            n //= i
if n != 1:
    print(n)