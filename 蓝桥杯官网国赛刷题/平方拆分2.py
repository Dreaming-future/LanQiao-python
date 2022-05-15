
from glob import glob
import sys
from math import sqrt
sys.setrecursionlimit(1<<31-1)
a = [i*i for i in range(1,50)]
length = len(a)

s = 0
ans = 0
def dfs(i):
    global s
    if s == 2019:
        global ans
        ans += 1
        return 
    elif s > 2019:
        return
    for j in range(i,length):
        s += a[j]
        dfs(j+1)
        s -= a[j]

dfs(0)
print(ans)