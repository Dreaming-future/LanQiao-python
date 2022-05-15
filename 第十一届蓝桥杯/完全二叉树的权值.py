import os
import sys
import math

# 请在此输入您的代码
n = int(input())
a = list(map(int,input().split()))
# 真实层数
x = int(math.log(n+1,2)) + 1
# 对不是完全二叉树补0
if x != n:
  a = a + [0] * (2**x - 1 - n)
ans = 0
# 位置
pos = 0
for i in range(x+1):
  cnt = sum(a[2**i-1:2**i-1 + 2**(i)])
  if cnt > ans:
    pos = i
    ans = cnt
print(pos+1)