# https://www.lanqiao.cn/problems/1595/learning/

n = int(input())
a = [0]
a += list(map(int,input().split()))
c = [] # 记录大于1的数字
f = [] # 记录大于1的数字的位置
s = 0 # 总数
presum = [0]*(n+1) # 前缀和数组
for i in range(1,n+1):
    presum[i] += a[i] + presum[i-1] # 计算前缀和
    if a[i]>1:  # 如果当前值大于1的情况
        c.append(a[i])  # 记录当前值
        f.append(i) # 记录位置
    else:
        s += 1 # 如果是为1，单独自己的区间就是合格的
    
# 从左边开始记录连续的1的个数，如果遇到不是1，直接设为0
ans = 0
l = [0]*(n+1)
for i in range(1,n+1):
    if a[i] == 1:
        l[i] = ans # 记录当前遇到的1的数
        ans += 1
    else:
        l[i] = ans
        ans = 0
# 从右边开始记录连续的1的个数，如果遇到不是1，直接设为0
ans = 0
r = [0]*(n+1)
for i in range(n,0,-1):
    if a[i] == 1:
        r[i] = ans # 记录当前遇到的1的数
        ans += 1
    else:
        r[i] = ans
        ans = 0
        
MAX = presum[n] + 2*n
cnt = len(c)
for i in range(cnt):
    cc = 1
    for j in range(i,cnt):
        cc *= c[j]
        if cc > MAX: break # 如果乘积大于，说明不可能存在
        lb = f[i] # 这是开始的左边界
        rb = f[j] # 这是开始的右边界
        ss = presum[rb] - presum[lb-1] # 得到这部分的铅缀和
        dd = cc - ss
        if dd == 0:
            s += 1 # 两者相同，直接计数
        # 如果两者不相同，并且存在足够的1，可能可以让两者乘积和累加相等
        elif dd>0 and dd<=l[lb]+r[rb]:
            xx = min(dd,l[lb]) # 左边最多可以给多少个 1
            yy = min(dd,r[rb]) # 右边最多可以给多少个 1
            s += xx+yy-dd+1; # 统计数字即可
print(s)