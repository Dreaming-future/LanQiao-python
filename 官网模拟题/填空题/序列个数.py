# https://www.lanqiao.cn/problems/584/learning/
import os
import sys
import itertools
# 请在此输入您的代码
cnt = 0
for i in itertools.combinations_with_replacement([x for x in range(1,11)], 5):
    if sorted(list(i)) == list(i):
        cnt += 1
print(cnt)