#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   202104-1.py
# @Time    :   2021/11/20 12:24:54
# @Author  :   DKJ
# @Contact :   1016617094@qq.com
# @Software:   VScode

# here put the import lib


n,m,L = map(int,input().split())
data = []
hist = [0] * L
for i in range(n):
    x = list(map(int,input().split()))
    for j in x:
        hist[j] += 1
print(' '.join(str(i) for i in hist))