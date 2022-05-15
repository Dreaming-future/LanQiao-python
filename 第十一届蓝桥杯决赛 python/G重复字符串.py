
k = int(input())
s = input()
n = len(s)
m = n//k # 得到一共有m个字
n = m*k # 测试数据出错
import collections
if n%k != 0: # 如果不能构成k个重复字符串，就无法改变
    print(-1)
else:
    ans = 0
    for i in range(m):
        c = collections.Counter(s[i:n:m])
        ans += k - max(c.values())
    print(ans)