

n,k = map(int,input().split())

a = list(map(int,input().split()))
maxa = max(a)
from collections import Counter

c = Counter(a)
if k == 0:
    print(len(c))
else:
    # dp[i]表示前i个积分能获得的最大用户数（不能匹配的）
    dp = [0]*(maxa+1)
    ans = 0
    for i in range(0,k):
        maxindex = 0
        # 这里相当于分组，分为{k,2k,3k....}
        # 希望在每一分组中选择尽可能多的客户
        for j in range(i,maxa+1,k):
            if j - 2*k >= 0:
                # 如果 j 不上线，则j-k上线
                # 如果 j 上线， 则不影响j-2*k，所以j-2k可以上线
                dp[j] = max(dp[j-2*k]+c[j],dp[j-k])
            elif j - k >= 0:
                dp[j] = max(dp[j-k],c[j])
            else:
                dp[j] = c[j]
            maxindex = j
        ans += dp[maxindex]
    print(ans)