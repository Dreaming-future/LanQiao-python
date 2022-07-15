# http://118.190.20.162/view.page?gpid=T130
import itertools
n = int(input())
arr=list(map(int,input().split()))
arr = [x for x,y in itertools.groupby(arr)]
arr = [0] + arr + [0]
# print(arr)

cnt = {}
L = len(arr)
for i in range(1,L-1):
    # 山峰
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        cnt[arr[i]] = cnt.get(arr[i],0) + 1 # 如果是山峰，则水平面降到arr[i]时，多一座山，答案加一
    # 山谷
    if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
        cnt[arr[i]] = cnt.get(arr[i],0) - 1 # 如果是山谷，则水平面降到arr[i]时，两山并为一山，答案减一
# print(cnt)
MAX = max(arr)
ans = 0
res = 0
for i in range(MAX,0,-1): # 水平面从最高处开始下降
    ans += cnt.get(i,0) # ans记录水平面为o时山的数量
    res = max(res,ans)
print(res)