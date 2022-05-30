#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   201909-1.py
# @Time    :   2021/11/20 12:24:49
# @Author  :   DKJ
# @Contact :   1016617094@qq.com
# @Software:   VScode

# here put the import lib

n,m = map(int,input().split())

data = []
max_c = 0
for i in range(n):
    x = list(map(int,input().split()))
    c = sum(x[1:])
    if c*-1 > max_c:
        max_c = c*-1
        index = i+1
    data.append(x[0]+c)
print(sum(data),index,max_c)

'''
example 1:
3 3
73 -8 -6 -4
76 -5 -10 -8
80 -6 -15 0

167 2 23

example 2:
2 2
10 -3 -1
15 -4 0

17 1 4
'''