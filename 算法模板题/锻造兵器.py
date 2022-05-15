'''
https://www.lanqiao.cn/problems/1374/learning/
难度: 简单   标签: 尺取法
'''

# n, C = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# opt = dict()
# cnt = 0
# for i in a:
#   cnt += opt.get(i-C, 0)
#   opt[i] = opt.get(i, 0)+1
# print(cnt)

n, c = map(int, input().split())
a = [int (i) for i in input().split()]
# 
length = len(a)
j = 0
k = 0
ans = 0
a.sort()
# print(a)
for i in range(0, length-1):  # a[lenght-1] 这是a的最后一个
    # 两者差不够c就往右走
    while j<=length-1 and a[j] - a[i] < c:
        j += 1
    # j的位置已经符合了或者略过了
    # 要能往下走 则是 j=length(越界) 或者  j <= length-1且符合 
    # 不可以放 j = i 因为 j一定在不等于位置 而k要在最后的位置
    while k <= length-1 and a[k] - a[i] <= c:
        k += 1
    # 它俩差正好为符合条件的数量    k的位置在符合之后  但k位置绝对符合
    if j <= length-1 and a[j] - a[i] == c and a[k-1] - a[i] and k >= 2:
        ans += k-j
print(ans)