import os
import sys


# 请在此输入您的代码
f = []
f.append(list(map(int,input().strip().split(' '))))
for i in range(1,29):
  f.append(list(map(int,input().strip().split(' '))))
  for j in range(len(f[-2])):
      w = f[-2][j] / 2
      f[-1][j] += w
      f[-1][j+1] += w
print(f[-1])
print(min(f[-1]))
print(int(2086458231/min(f[-1])*max(f[-1])))
input()