import os
import sys

# https://www.lanqiao.cn/problems/227/learning/
from itertools import *
a = input()
a = list(a)
kn = []

"""
枚举最终的状态TAB,TBA等六种, 假设当前枚举的是TAB
答案 = T区间的AB数 + B区间的TA数 - min(T区间的B数，B区间的T数)
"""
for i in permutations(["B","A","T"]):
    kn.append(list("".join(i)))

def solve(s, zm_list):
    front  = s.count(zm_list[0])
    rear = s.count(zm_list[2])

    front_0 = s[:front].count(zm_list[0])
    front_2 = s[:front].count(zm_list[2])
    
    rear_0 = s[-rear:].count(zm_list[0])
    rear_2 = s[-rear:].count(zm_list[2])
    
    res = (front - front_0) + (rear - rear_2) - min(front_2, rear_0)
    return res

ans = float('inf')
for i in kn:
    res = solve(a,i)
    ans = min(ans,res)
print(ans)