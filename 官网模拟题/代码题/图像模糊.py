# https://www.lanqiao.cn/problems/550/learning/

n,m = map(int,input().split())
mat = [[0]*(m+2)]

for i in range(n):
    mat.append([0]+list(map(int,input().split()))+[0])
mat.append([0]*(m+2))
for i in range(1,n+1):
    for j in range(1,m+1):
        ans = 0
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                ans += mat[x][y]
        if (i==1 and (j==1 or j==m)) or (i==n and (j==1 or j==m)):
            ans = ans//4
        elif i==1 or j==1 or i==n or j==m:
            ans = ans//6
        else:
            ans = ans//9
        print(ans,end=' ')
    print()