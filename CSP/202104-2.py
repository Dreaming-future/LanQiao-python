# http://118.190.20.162/view.page?gpid=T127

n,L,r,t = map(int,input().split())
A = [[0]*(n+2)]
for i in range(n):
    A.append([0] + list(map(int,input().split())) + [0])
A.append([0]*(n+1))

b = [[0]*(n+2) for i in range(n+2)]

for i in range(1,n+1):
    for j in range(1,n+1):
        b[i][j] = b[i-1][j] + b[i][j-1] - b[i-1][j-1] + A[i][j] # 处理前缀和矩阵
        
sum = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        x1 = max(i-r,1)
        y1 = max(j-r,1)
        x2 = min(i+r,n)
        y2 = min(j+r,n)
        ans = (x2-x1+1)*(y2-y1+1) # 领域内的个数
        if (b[x2][y2] + b[x1-1][y1-1] - b[x1-1][y2] - b[x2][y1-1])/ans  <= t:
            sum += 1
print(sum)