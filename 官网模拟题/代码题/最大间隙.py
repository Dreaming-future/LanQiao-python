# https://www.lanqiao.cn/problems/543/learning/
n = int(input())
nums = list(map(int,input().split()))

ans = 0
for i in range(n-1):
    ans = max(ans,num[i+1]-nums[i])
print(ans)