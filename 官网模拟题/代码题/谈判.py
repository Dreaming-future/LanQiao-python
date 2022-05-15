
# https://www.lanqiao.cn/problems/545/learning/
n = int(input())
t = list(map(int,input().split()))
t.sort()
ans = 0
for i in range(n-1):
    ans += t[i]+t[i+1]
    t[i+1] = t[i] + t[i+1]
    t.sort()
print(ans)