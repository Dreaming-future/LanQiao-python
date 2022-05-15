'''
https://www.lanqiao.cn/problems/1231/learning/
难度: 简单   标签: 计算几何基础
'''

import math
def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
t = int(input())
for _ in range(t):
    p = []
    for _ in range(3):
        x_,y_ = map(int,input().split())
        p.append([x_,y_])
    a = dist(p[0],p[1])
    b = dist(p[2],p[1])
    c = dist(p[0],p[2])
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("{:.2f}".format(s))