# https://www.lanqiao.cn/problems/1375/learning/
# 难度: 简单   标签: 倍增
from collections import deque


N, M = map(int, input().split())
a = [int(v) for v in input().split()]

Q = deque()
res = []
for i, v in enumerate(a):
    while Q and Q[0] <= i - M:
        Q.popleft()
    while Q and a[Q[-1]] >= v:
        Q.pop()
    Q.append(i)
    if i >= M - 1:
        res.append(a[Q[0]])
print("\n".join(map(str, res)))