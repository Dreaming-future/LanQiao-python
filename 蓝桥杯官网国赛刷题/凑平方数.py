
from collections import Counter

a = []
def check(x):
    c = Counter(str(x))
    for i in c.values():
        if i > 1:
            return False
    return True

for i in range(100000):
    if check(i*i):
        a.append(i*i)


def judge(c):
    if len(c) != 10:
        return  False
    for i in c.values():
        if i != 1:
            return False
    return True

length = len(a)
vis = [0]*len(a)

ans = 0
def dfs(i,c,s):
    # 符合条件
    if judge(c):
        for x in s:
            print(a[x],end=' ')
        print()
        global ans
        ans += 1
            
    for j in range(i+1,length):
        if vis[j] == 0:
            vis[j] = 1
            C =  (c  + Counter(str(a[j])))
            flag = True
            for k in C.values():
                if k > 1:
                    flag=False
                    break
            if flag:
                s.add(j)
                dfs(j,C,s)
                s.remove(j)
            vis[j] = 0

for i in range(length):
    vis[i] = 1
    s = set()
    s.add(i)
    dfs(i,Counter(str(a[i])),s)
    vis[i] = 0
print(ans)