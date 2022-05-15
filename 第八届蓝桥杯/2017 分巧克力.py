N,K = list(map(int,input().split()))
H = []
W = []
for i in range(N):
    h,w = list(map(int,input().split()))
    H.append(h)
    W.append(w)
l = 0
r = 100000
while l <= r:
    cnt = 0
    mid = (l+r)//2
    for j in range(N):
        cnt += (H[j]//mid)*(W[j]//mid)
    
    if cnt >= K:
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)
