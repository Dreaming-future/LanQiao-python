import os
import sys

# 请在此输入您的代码

n,k = map(int,input().split())
a  = []
for i in range(k):
  a.append(int(input()))

a.sort() # a数组进行排序
def check(d):
    last=0 # 覆盖长度
    for i in range(k):
        if last + d >= a[i]: # 是否到达的了a[i]
            if last > a[i]:
                last = a[i] + d - 1 
            else:
                last += d
        else:
            return False
    return last >= n 


l,r = 1,n
while l < r:
  mid = (l+r)>>1
  if check(mid):
      r = mid
  else:
      l = mid + 1

print((l-1)*2) # 2 * 走的格数