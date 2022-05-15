'''
https://www.lanqiao.cn/problems/1177/learning/
难度: 简单   标签: dp, 背包, 混合背包
'''

# N,V = map(int,input().split())

# # f[i][j]表示前i种，总体积不超过j，最大的总价值
# f = [[0]*(V+1) for _ in range(N+1)]


# for i in range(1,N+1):
#     v,w,s = map(int,input().split())
#     for j in range(1,V+1):
#         # 多重背包的区别就是，不可以直接简化，因为数量已经有了限制，所以说独立一个循环进行判断和更新
#         if s != 0:
#             for k in range(s+1):
#                 if k*v <= j:
#                     # 这一部分判断，是否买k个
#                     f[i][j] = max(f[i][j],f[i-1][j-k*v] + k*w)
#                 else:
#                     break
#         else:
#             k = 0
#             while k*v <= j:
#                 f[i][j] = max(f[i][j],f[i-1][j-k*v] + k*w)
#                 k += 1
# print(f[N][V])


N,V = map(int,input().split())
v = [0]*12010
w = [0]*12010
f = [0]*12010
cnt = 0
for i in range(N):
    a,b,s = map(int,input().split())
    if s == 0:
        s = V//a # 设置上界即可
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