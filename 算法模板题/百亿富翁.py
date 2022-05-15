'''
https://www.lanqiao.cn/problems/1142/learning/
难度: 简单   标签: 单调栈
'''

n = int(input())
h = list(map(int,input().split()))

sl = []
sr = []

l = [-1]*n
for i in range(n):
    while sl and h[sl[-1]] <= h[i]:
        sl.pop()
    if sl:
        l[i] = sl[-1] + 1
    sl.append(i)
    
r  = [-1]*n
for i in range(n-1,-1,-1):
    while sr and h[sr[-1]] <= h[i]:
        sr.pop()
    if sr:
        r[i] = sr[-1] + 1
    sr.append(i)
    
print(" ".join(map(str,l)))
print(" ".join(map(str,r)))
