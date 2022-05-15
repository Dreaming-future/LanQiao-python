# https://www.lanqiao.cn/problems/185/learning/

import os
import sys

# 并查集 用于处理元素分组 寻找父亲
def find(x):
    global fa
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

N = int(input())
A = list(map(int,input().split()))

# 首先创建数组大小的并查集序列 自循环 全部指向自己
fa = [i for i in range(1000001)]

for i in range(N):
    # 找到A[i]元素父亲
    # 如果A[i]元素没有找到 则返回A[i]的值 同时将下一次查到A[i]值指向A[i]指向下一位
    # 如果A[i]找到 则继续增加
    # 2 1 1 3 4
    # 首先2 的父亲是2 并同时把父亲数组中A[i]位置元素修改为3，也就是再遇到2的时候，换为3
    # 其次为1 1的父亲是1 同时把父亲数组中1位置元素修改为2
    # 获得1 1的父亲此时为3 输出3 并将3的父亲修改为4
    # 获得3 3的父亲此时为4 输出4 并将此时3的父亲修改为5
    # 获得4 4的父亲此时为5 输出5 并将此时5的父亲修改为6
    A[i] = find(A[i])
    fa[A[i]] = find(A[i] + 1) # 更新为下一个点指向的点

for i in range(N):
    print(A[i], end=" ")