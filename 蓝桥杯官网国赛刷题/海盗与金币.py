import os
import sys


def dfs(step):
    if step == 12:
        return True
    blood = 0
    for i in range(12):
        if i == step: continue
        if a[i]%2 != 0: return False
        blood += a[i]/2
        a[i] = a[i]/2
    a[step] += blood
    if dfs(step+1):
        return True
    else:
        return False

for i in range(49000,51000):
    if i % 12  == 0:
        val = i // 12
        a = [val] * 12
        if dfs(0):
            print(list(map(int,a)))

            break
            
        