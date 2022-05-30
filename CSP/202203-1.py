
n,k = map(int,input().split())

a,b = [],[]

vis = [0 for i in range(n+1)]
vis[0] = 1
ans = 0
for i in range(k):
    x,y = map(int,input().split())
    if not vis[y]:
        ans += 1
    vis[x] = 1
    
print(ans)
    