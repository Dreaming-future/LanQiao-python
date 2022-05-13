import os
import sys

# 请在此输入您的代码

from itertools import permutations as p

a =[i for i in range(10)]
s = []
for x in p(a):
  if x[0] == 0 or x[4] == 0 or x[8] == 0:
    continue
  s1 = x[0]*1000 + x[1]*100 + x[2]*10 + x[3]
  s2 = x[4]*1000 + x[5]*100 + x[6]*10 + x[7]
  s3 = x[8]*10 + x[9]
  if (s1 - s2)*s3 == 900:
    print(s1)
    s.append(s1)
print(s)