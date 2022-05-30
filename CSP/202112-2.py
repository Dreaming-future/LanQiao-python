# http://118.190.20.162/submitlist.page?gpid=T137

# 输入的数据
n,N = map(int,input().split())
A = [0]
A.extend(list(map(int,input().split())))
A.append(N)
r = N // (n+1)
B = []
for i in range(N//r + 2):
    if i*r >= N: break 
    B.append(i*r)
B.append(N)
s = list(set(A+B))
s.sort()
L = len(s)
# 离散化
tree = [0]*(L-1)
from bisect import bisect_left as bl
for i in range(len(A) - 1):
    a,b = bl(s,A[i]),bl(s,A[i+1])
    for j in range(a,b):
        tree[j] += i

for i in range(len(B) - 1):
    a,b = bl(s,B[i]),bl(s,B[i+1])
    for j in range(a,b):
        tree[j] -= i
# tree求两边的差值的划分
ans = 0
for i in range(L-1):
    # tree[i]代表的是差值，s[i+1] - s[i]代表的是区间的长度
    ans += abs(tree[i]*(s[i+1]-s[i]))
print(ans)