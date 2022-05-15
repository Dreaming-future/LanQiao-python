# https://www.lanqiao.cn/problems/585/learning/

s = 'lanqiao'
n = len(s)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        ans += abs(ord(s[j])-ord(s[i]))
print(ans)