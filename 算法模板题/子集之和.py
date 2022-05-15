'''
https://www.lanqiao.cn/problems/1220/learning/
难度: 简单   标签: 折半查找
'''

import sys
sys.setrecursionlimit(1<<31-1)
n,x = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
# 传入下标 和 总数
def dfs(index,total):
    if total == x:
        return True
    if total > x:
        return False
    # 从index+1开始遍历，查找之后所有的整数，进行dfs执行递归
    for i in range(index+1,n):
        if dfs(i,total+s[i]):
            return True
    return False

flag = True
for i in range(n):
    if dfs(i,s[i]):
        flag = False
        print('Y')
        break
if flag:
    print('N')