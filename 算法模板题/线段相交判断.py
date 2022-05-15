'''
https://www.lanqiao.cn/problems/1287/learning/
难度: 简单   标签: 计算几何基础
'''

import os
import sys

# 请在此输入您的代码
#Python3.6
class point(): #定义类
    def __init__(self,x,y):
        self.x=x
        self.y=y   

def cross(p1,p2,p3):#跨立实验
    x1=p2.x-p1.x
    y1=p2.y-p1.y
    x2=p3.x-p1.x
    y2=p3.y-p1.y
    return x1*y2-x2*y1     

def IsIntersec(p1,p2,p3,p4): #判断两线段是否相交

    #快速排斥，以l1、l2为对角线的矩形必相交，否则两线段不相交
    if(max(p1.x,p2.x)>=min(p3.x,p4.x)    #矩形1最右端大于矩形2最左端
    and max(p3.x,p4.x)>=min(p1.x,p2.x)   #矩形2最右端大于矩形最左端
    and max(p1.y,p2.y)>=min(p3.y,p4.y)   #矩形1最高端大于矩形最低端
    and max(p3.y,p4.y)>=min(p1.y,p2.y)): #矩形2最高端大于矩形最低端

    #若通过快速排斥则进行跨立实验
        if(cross(p1,p2,p3)*cross(p1,p2,p4)<0
           and cross(p3,p4,p1)*cross(p3,p4,p2)<0):
            D=2
        elif (cross(p1,p2,p3)*cross(p1,p2,p4)==0
           and cross(p3,p4,p1)*cross(p3,p4,p2)==0):
            D=1
        else:
            D=0
    else:
        D=0
    return D

t=int(input())
for i in range(t):
    p1,p2,p3,p4=point(0,0),point(0,0),point(0,0),point(0,0)
    x=list(map(float,input().split()))
    y=list(map(float,input().split()))
    p1.x,p1.y=x[0],x[1]
    p2.x,p2.y=x[2],x[3]
    p3.x,p3.y=y[0],y[1]
    p4.x,p4.y=y[2],y[3]
    print(IsIntersec(p1,p2,p3,p4))