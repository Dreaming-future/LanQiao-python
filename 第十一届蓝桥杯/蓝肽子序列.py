# https://www.lanqiao.cn/problems/1030/learning/

s1 = input()
s2 = input()

S1,S2 = [],[]
a,b = '',''

for s in s1:
    if 'A' <= s <= 'Z':
        if a!= '':
            S1.append(a)
        a = ''
    a += s
S1.append(a)

for s in s2:
    if 'A' <= s <= 'Z':
        if b!= '':
            S2.append(b)
        b = ''
    b += s
S2.append(b)
# print(S1,S2)

n = len(S1)
m = len(S2)

dp = [[0]*(m+1) for _ in range(n+1)]

# 动态规划的求解最大公共序列
for i in range(1,n+1):
    for j in range(1,m+1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])