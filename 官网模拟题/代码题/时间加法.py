# https://www.lanqiao.cn/problems/548/learning/
import os
import sys

# 请在此输入您的代码
a = int(input())
b = int(input())
t = int(input())
b = t + b
a = (a + b //60)%24
b = b%60
print(a)
print(b)