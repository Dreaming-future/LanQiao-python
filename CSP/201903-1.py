#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   201903-1.py
# @Time    :   2021/11/20 17:48:05
# @Author  :   DKJ
# @Contact :   1016617094@qq.com
# @Software:   VScode

# here put the import lib
n = int(input())

l = list(map(int,input().split()))
l.sort()

if n % 2 == 1:
    mid = l[n//2]
else:
    mid = l[n//2] + l[n//2 -1 ]
    mid = mid / 2
    if mid *10 %10 == 0:
        mid = int(mid)
print(l[-1],'%.1f'%mid if type(mid) == float else mid,l[0])