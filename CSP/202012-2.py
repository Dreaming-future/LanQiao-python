# http://118.190.20.162/view.page?gpid=T122
# 前缀和 + 后缀和，只使用前缀和也可以，这样可以更快
a = [(-1,-1)]
m = int(input())
for _ in range(m):
    yi,resi = map(int,input().split())
    a.append((yi,resi))
    
a.sort()
pre0 = [0]*(m+2) # 记录该位置及前面的result为0的个数（前缀和）
# rear1 = [0]*(m+2) # 记录该位置及后面的result为1的个数（后缀和）

for i in range(1,m+1):
    if a[i][1] == 0:
        pre0[i] = pre0[i-1] + 1
    else:
        pre0[i] = pre0[i-1]

# for i in range(m,0,-1):
#     if a[i][1] == 1:
#         rear1[i] = rear1[i+1] + 1
#     else:
#         rear1[i] = rear1[i+1]

ans = 0
res = 0
for i in range(1,m+1):
    if a[i][0] == a[i-1][0]:
        continue # 如果有阈值相同的情况，那么在相同区间的第一个位置统计了，直接跳过
    x = pre0[i-1] + ((m - i + 1) - (pre0[m]-pre0[i-1])) # 前者是 0 的个数，后者是 1 的个数
    if ans <= x:
        ans = x
        res = a[i][0]
print(res)