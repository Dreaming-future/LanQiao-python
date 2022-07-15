# http://118.190.20.162/view.page?gpid=T125
from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
N = 1010
MOD = int(1e9+7)
'''
设f[i]为前i个障碍物所能生成的最多可能性
设 cnt[i][j]为从第i个障碍物到第j个障碍物的可行方案数
想要求cnt[i][j]只需从位置i枚举所有间隔的可能性,看是否能在不触碰到i,j之间的障碍物的情况下到达
'''

f = [0]*N
f[0] = 1

q = defaultdict(list)
M = 100010
for i in range(1,M):
    for j in range(2*i,M,i):
        q[j].append(i)

# 动态规划
for i in range(1,n): # 每轮添加一个障碍物，计算添加后的方案总数
    st = defaultdict(int) # 清空状态数组
    for j in range(i-1,-1,-1):
        d = a[i] - a[j]
        cnt = 0
        for k in q[d]: # 枚举d的所有的因子，也就是所有可能的方案
            if not st[k]: # 如果此因子之前没使用过，方案数加一，并标记当前因子已被用过
                cnt += 1
                st[k] = 1
        # 手动添加d本身，因为下一轮如果按照这个间隔植树就会撞上本轮添加的障碍物
        st[d] = 1 # 因为最后一个障碍物必选
        f[i] = (f[i] + f[j]*cnt)%MOD
        
print(f[n-1])