# # https://www.lanqiao.cn/problems/1593/learning/

# from math import comb
# n,k = map(int,input().split())

# def lowbit(x):
#     return x&(-x)

# one,zero = 0,0
# x = n
# while x:
#     if x&1:
#         one += 1
#     else:
#         zero += 1
#     x >>= 1
    
# ans = 0
# if one == k:
#     ans += 1
    

# while n != 0:
#     x = lowbit(n)
#     n -= lowbit(x)
#     one -= 1
#     m = k - one # 还需要的1
#     cnt = 0
#     while x:
#         cnt += 1
#         x >>= 1
#     if k >= 0: # 如果大于等于0
#         ans += comb(cnt - 1,m) # 除了之前的位置上的 1 变成 0 的情况

# print(ans)
import sys
sys.setrecursionlimit(1<<31-1)
N = 63
f = [[-1]*N for _ in range(N)]
a = [0]*N


# pos 当前枚举到的位
# cnt 是1的个数，也就是当前状态
# limit 表示当前位是否可以任选
def dp(pos, cnt, limit):
    if not pos: return cnt == k # 判断当前位
    # 记忆化,在可以任选的情况下如果当前状态的值已经被计算过则可以直接返回
    if not limit  and f[pos][cnt] != -1: return f[pos][cnt] 
    up = a[pos] if limit else 1 # 根据limit判断上界，因为是二进制，所以是最大上界是1，进制-1
    ans = 0
    # 枚举每一位并且记录答案
    for i in range(up+1):
        # 状态转移方程
        ans += dp(pos-1,cnt+(i==1),limit and (i==up))
    # limit为False，就进行记录
    if not limit:
        f[pos][cnt] = ans
    return ans

def solve(x):
    pos = 0
    # 把数拆分至a数组中 
    while x:
        pos += 1
        a[pos] = x%2 # x % 进制
        x = x//2 # x / 进制
    # 从最高位开始枚举，刚开始默认为有限制
    return dp(pos,0,1)

n,k = map(int,input().split())
res = solve(n)
print(res)


'''
对于limit的理解：假如我们当前遍历到第pos位，那么当前位置的取值有两种可能性：

（1）如果pos前面某一位已经小于上限数字对应位置的数字，这一位可以填0~进制数-1

（2）如果pos前面每一位都等于上限数字对应位置的数字，这一位可填充数字范围位0~上限数字对应位置的数字

而limit就是维护前面每一位是否和上限数字一样，就可以得到当前位置数字可填范围，也是可以进行记忆化搜索的条件
'''