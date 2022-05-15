
n,m = 2,3
b = [[-1]*m for i in range(n)]



def check():
    for i in range(3-1):
        for j in range(10-1):
            if b[i][j] + b[i+1][j] + b[i][j+1] + b[i+1][j+1] % 4 == 0:
                return False
    return True

ans = 0
# 0 表示黄色， 1 表示蓝色
def dfs(x,y):
    if x == n and y == m:
        if check():
            ans += 1
            return
    
    # 横纵都是按行铺的，所有都有越界风险
    if b[x][y] == -1:
        # 横着放
        if y + 1 < m and b[x][y] == -1:
            b[x][y] = b[x][y+1] = 0 # 黄色瓷砖
            if y == 10:# 判断该行是否铺满了
                dfs(x+1,0)
            else:
                dfs(x,y+1)
            b[x][y] = b[x][y+1] = -1
            
            b[x][y] = b[x][y+1] = 1 # 橙色瓷砖
            
            if y == m:# 判断该行是否铺满了
                dfs(x+1,0)
            else:
                dfs(x,y+1)
            
            b[x][y] = b[x][y+1] = -1
            
        # 竖着放
        if x + 1 < n and b[x][y] == -1:
            b[x][y] = b[x+1][y] = 0
            if y == m: 
                dfs(x+1,0)
            else: 
                dfs(x,y+1)
            b[x][y] = b[x+1][y] = -1
            
            b[x][y] = b[x+1][y] = 1
            if y == m: 
                dfs(x+1,0)
            else: 
                dfs(x,y+1)
            b[x][y] = b[x+1][y] = -1
    if y == m:
        dfs(x+1,0)
    else:
        dfs(x,y+1)

dfs(0,0)
print(ans)