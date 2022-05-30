#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   202006-1.py
# @Time    :   2021/11/20 12:24:38
# @Author  :   DKJ
# @Contact :   1016617094@qq.com
# @Software:   VScode

n,m = map(int,input().split(' '))
data = []
for i in range(n):
    # 将输入数据压入data
    data.append(list(input().split(' ')))
    
def f(z,x,y,X,Y):
    # 得到直线方程
    return z + x*X + y*Y

for i in range(m):
    key = {}
    count = {}
    z,x,y = map(int,input().split())
    
    if f(z,x,y,int(data[0][0]),int(data[0][1])) > 0:
        key['A'] = 1
        key['B'] = -1
    else:
        key['A'] = -1
        key['B'] = 1
    flag = 1
    for j in range(1,n):
        # 如果是正确分类的话，满足f*key > 0,key是进行符号变换的
        if f(z,x,y,int(data[j][0]),int(data[j][1])) * key[data[j][2]] < 0:
            flag = 0
            break
        else:
            count[key[data[j][2]]] = 1
    # 子任务，A和B都要存在，如果不存在也是No
    if 'A' and 'B' not in count.keys():
        flag = 0
    if flag:
        print('Yes')
    else:
        print('No')