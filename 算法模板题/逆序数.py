'''
https://www.lanqiao.cn/problems/1263/learning/
'''

import os
import sys
sys.setrecursionlimit(1<<31-1)
# 请在此输入您的代码
n = int(input())

a = list(map(int,input().split()))
t = [0]*(n+1)
ans = 0
def msort(left, right):
    global ans 
    if left == right:
        return 
    mid = (left + right)>>1
    msort(left,mid)
    msort(mid + 1, right)
    l = left
    r = mid + 1
    k = l
    while l <= mid and r <= right:
        if a[l] <= a[r]:
            t[k] = a[l]
            k +=1
            l += 1
        else:
            t[k] = a[r]
            k +=1 
            r += 1
            ans += mid - l + 1
    while l <= mid:
        t[k] = a[l]
        k +=1
        l += 1
    while r <= right:
        t[k] = a[r]
        k +=1
        l += 1
    for i in range(left, right +1):
        a[i] = t[i]

msort(0,n-1)
print(ans)
          