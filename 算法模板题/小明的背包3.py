'''
https://www.lanqiao.cn/problems/1176/learning/
难度: 简单   标签: dp, 背包, 多重背包
'''
# import os
# import sys

# # 请在此输入您的代码

# N,V = map(int,input().split())

# # 多重背包和完全背包是一样的构造方式
# f = [[0]*(V+1) for _ in range(N+1)] 

# for i in range(1,N+1):
#     v,w,s = map(int,input().split())
#     for j in range(1,V+1):
#         # 多重背包的区别就是，不可以直接简化，因为数量已经有了限制，所以说独立一个循环进行判断和更新
#         for k in range(s+1):
#             if k*v <= j:
#                 # 这一部分判断，是否买k个
#                 f[i][j] = max(f[i][j],f[i-1][j-k*v] + k*w)
#             else:
#                 break
# print(f[N][V])



# 多重背包二进制还可以进行优化，要不然上一部分的复杂度有 On的三次方
# 会把多重背包转化为01背包，对于01背包就稍微简单一点
# 比如200个数量的物体，可以转为为1,2,4,8,....,64,74这么多组
# 因为1~127的数可以由1~64构成，然后200-127 = 73 
# （1~127 都可以表示出来，选出任意一种与 73 组合就可以表示出 74 ~ 200 ，所以合起来就可以表示 1~200）。
# 相当于每个数量的为一组

N,V = map(int,input().split())
v = [0]*12010
w = [0]*12010
f = [0]*12010

cnt = 0
for i in range(N):
    a,b,s = map(int,input().split())
    k = 1
    # 按照二进制的形式分组
    while k <= s:
        cnt += 1
        v[cnt] = k*a
        w[cnt] = k*b
        s = s - k
        k = k*2
    # 不能按照二进制分组的物体数量单独划分为一组。
    if k > 0:
        cnt += 1
        v[cnt] = a*s
        w[cnt] = b*s

# 分组后就等同于0 1 背包
for i in range(1,cnt + 1):
    for j in range(V,0,-1):
        if j >= v[i]:
            f[j] = max(f[j],f[j-v[i]] + w[i])
        else:
            break

print(f[V])