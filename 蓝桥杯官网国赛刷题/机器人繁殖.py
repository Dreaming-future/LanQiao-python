import os
import sys

# 请在此输入您的代码


n,s = map(int,input().split())

x = 2**(n+1) - 1
res = (s+x-n-1)// x 
print(res)