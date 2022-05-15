'''
https://www.lanqiao.cn/problems/1136/learning/
难度: 简单   标签: 种类并查集
'''

import os
import sys

# 请在此输入您的代码
n,m = map(int,input().split())

# 用一半来维护朋友关系，另一半用来维护敌人关系
f = [i for i in range(2*n+1)] # 种类并查集
def find(x):
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]

def union(x,y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        f[fy] = fx


for _ in range(m):
    x,y = map(int,input().split())
    # 判断是否是朋友，或者是敌人的敌人，就是朋友，这样就说明有问题
    if find(x) == find(y) or find(x+n) == find(y+n):
        print(x)
        break
    # 对于1个编号为i的元素，i+n是它的敌人
    union(x,y+n) # 维护敌人关系
    union(x+n,y) # 维护敌人关系
  