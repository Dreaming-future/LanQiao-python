'''
https://www.lanqiao.cn/problems/1228/learning/
难度: 简单   标签: 哈夫曼树, 贪心
'''

import os
import sys
from heapq import *
# 请在此输入您的代码
n = int(input())
stamps = list(map(int,input().split()))
heapify(stamps)
ans = 0
while len(stamps) > 1:
    x = heappop(stamps)
    y = heappop(stamps)
    ans += x+y
    heappush(stamps,x+y)
print(ans)
