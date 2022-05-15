


# 染色
def fill(x,y,n,num):
    for i in range(x,x+n):
        for j in range(y,y+n):
            mp[i][j] = num

# 判断是否染色完毕
def solve():
    for i in range(154):
        for j in range(154):
            if not mp[i][j]: # 如果没有染色的话
                return False
    return True

# 判断是否可写
def judge(x,y,n):
    if x+n>154 or y+n>154:
        return False
    for i in range(x,x+n):
        for j in range(y,y+n):
            if mp[i][j]:
                return False
    return True

def dfs(x,y):
    if solve():
        return True
    flag = True
    for i in range(154):
        if not flag: break
        for j in range(154):
            if not mp[i][j]:
                x = i
                y = j
                flag = False
                break
    for k in range(19):
        if judge(x,y,a[k]):
            if not vis[k]:
                fill(x,y,a[k],a[k])
                vis[k] = 1
                if dfs(x,y+a[k]):
                    return True
                fill(x,y,a[k],0)
                vis[k] = 0
        else:
            break
    return False

a = [2,5,9,11,16,17,19,21,22,24,26,30,31,33,35,36,41,50,52]
vis = [0]*19
mp = [[0]*154 for i in range(154)]
fill(0,0,47,47)
fill(0,47,46,46)
fill(0,93,61,61)
dfs(0,0)
ans = 0
for i in range(154):
    if mp[153][i] != ans:
        print(mp[153][i],end = ' ')
        ans = mp[153][i]
 