



n = 6
used = [[0]*n for i in range(n)]
ans = 0
path = []

f = [(1,0),(0,1),(-1,0),(0,-1)]

def check(x,y):
    if 0<= x < n and 0 <=y< n:
        return True
    return False

def dfs(x,y,step):
    if step > 12:
        return
    elif x == 0 and y == 0 and step > 2:
        global ans
        ans += 1
        return 
    for fx,fy in f:
        xi = fx + x
        yi = fy + y
        if check(xi,yi) and used[xi][yi] == 0:
            used[xi][yi] = 1
            path.append((xi,yi))
            dfs(xi,yi,step+1)
            path.pop()
            used[xi][yi] = 0

path.append((0,0))
dfs(0,0,0)
print(ans)
            