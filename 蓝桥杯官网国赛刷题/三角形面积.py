import os
import sys

# 请在此输入您的代码

def dis(x,y):
    x1,x2 = x
    y1,y2 = y
    return ((x1 - y1)**2 + (x2 - y2)**2)**0.5


a = dis((2.3,2.5),(6.4,3.1))
b = dis((2.3,2.5),(5.1,7.2))
c = dis((6.4,3.1),(5.1,7.2))

p = (a+b+c)/2
from math import sqrt
s = sqrt(p*(p-a)*(p-b)*(p-c))
print("{:.3f}".format(s))
