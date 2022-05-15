'''
https://www.lanqiao.cn/problems/1178/learning/
难度: 简单   标签: dp, 背包, 分组背包
'''

# N,V = map(int,input().split())

# f = [0]*(V+1)
# v = [[0]]
# w = [[0]]
# s = [0]
# for i in range(1,N+1):
#     s.append(int(input()))
#     # 一组物品只能买一件
#     vi = [0]
#     wi = [0]
#     for _ in range(s[i]):
#         a,b = map(int,input().split())
#         vi.append(a)
#         wi.append(b)
#     v.append(vi)
#     w.append(wi)

# # f[i][j] 代表在选择i组中， 体积不超过j的最大价值
# f = [[0]*(V+1) for _ in range(N+1)]
# for i in range(1,N+1): # 1~N 组数
#     for j in range(V,-1,-1): # V~0 体积数
#         for k in range(1,s[i]+1): # 1~i 分组的物品数
#             if j >= v[i][k]:
#                 f[i][j] = max(f[i][j],f[i-1][j - v[i][k]] + w[i][k])

# print(f[N][V])

# 压缩成一维
N,V = map(int,input().split())

f = [0]*(V+1)
v = [[0]]
w = [[0]]
s = [0]
for i in range(1,N+1):
    s.append(int(input()))
    # 一组物品只能买一件
    vi = [0]
    wi = [0]
    for _ in range(s[i]):
        a,b = map(int,input().split())
        vi.append(a)
        wi.append(b)
    v.append(vi)
    w.append(wi)
    
# f[i][j] 代表在选择i组中， 体积不超过j的最大价值
f = [0]*(V+1)
for i in range(1,N+1): # 1~N 组数
    for j in range(V,-1,-1): # V~0 体积数
        for k in range(1,s[i]+1): # 1~i 分组的物品数
            if j >= v[i][k]:
                f[j] = max(f[j],f[j - v[i][k]] + w[i][k])

print(f[V])