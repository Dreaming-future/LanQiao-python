#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   201912-1.py
# @Time    :   2021/11/20 17:21:48
# @Author  :   DKJ
# @Contact :   1016617094@qq.com
# @Software:   VScode

n = int(input())

i = 1
data = [0]*4
while i <= n :
    if i % 7 == 0 or '7' in str(i):
        data[i%4]+= 1
        n += 1
    
    i += 1
    
print('\n'.join(str(i) for i in data[1:]))
print(data[0])
'''
example1
20
2
1
1
0

example2:
66
7
5
11
5
'''