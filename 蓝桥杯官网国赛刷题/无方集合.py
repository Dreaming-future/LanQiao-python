

x = [i*i for i in range(1,16)]

s = []

for i in range(1,101):
    if i not in x:
        s.append(i)

vis = [0]*len(s)


def check(a):
    l = len(a)
    for i in range(l):
        for j in range(i+1,l):
            if (a[i] + a[j]) in x:
                return False
    return True

ans = 0
arr = []
def dfs(pos,step):
    global ans,arr
    ans = max(ans,step)
    for i in range(pos,len(s)):
        if vis[i] == 0:
            arr.append(s[i]) --
            if check(arr):
                vis[i] = 1
                dfs(i,step + 1)
                vis[i] = 0
            arr.pop()
                
dfs(0,0)
print(ans)