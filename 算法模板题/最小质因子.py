'''
https://www.lanqiao.cn/problems/1151/learning/
难度: 简单   标签: 埃氏筛
'''


import os
import sys
import bisect
import time
def prime():
    p = [1]*3000001
    p[0] = p[1] = 0
    for i in range(3000001):
        if p[i]:
            for i in range(2*i,3000001,i):
                p[i] = 0
    return p


t = int(input())
s = time.time()
dp  = [float('inf')]*3000001
dp[0] = dp[1] = 0
p = prime()
for _ in range(t):
    n = int(input())
    x = bisect.bisect_left(dp,float('inf'))
    if dp[x-1] != float('inf'):
        ans = dp[x-1]
    else:
        ans = 0
    for i in range(x,n+1):
        if p[i]:
            ans += i
            dp[i] = ans 
        else:
            for j in range(2,int(n**0.5)+1):
                if i%j == 0:
                    ans += j
                    dp[i] = ans
                    break
    print(ans)
    
print(time.time()-s)