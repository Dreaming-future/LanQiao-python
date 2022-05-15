
n,m = map(int,input().split())
a,b = [0],[0]
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

def check(x):
    cnt = 0
    for i in range(1,n+1):
        if a[i] <x: continue
        cnt += 1 + (a[i] - x)//b[i]
        if cnt >= m:
            return True

    return False

res = 0
l = 0
r = int(1e6)
while l <r:
    mid = l + r + 1 >> 1
    if check(mid):
        l = mid
    else:
        r = mid - 1

x = l
cc = 0
for i in range(1,n+1):
    t = 0
    if a[i] < x: continue
    t = (a[i]-x) // b[i] + 1
    if a[i] - (t-1)*b[i] == x:
        t-=1
        cc+=1
    if m >= t:
        m-=t
        res += t * (a[i] + a[i] - (t - 1) * b[i]) // 2
    else:
        t = m
        m = 0
        res += t * (a[i] + a[i] - (t - 1) * b[i]) // 2;
        break
res = res + min(m,cc) * x
print(res)
            
