# http://118.190.20.162/view.page?gpid=T112

n,k,t,xl,yd,xr,yw = map(int,input().split())

def check(x,y):
    if xl <= x <= xr and yd <= y <= yw:
        return True

sum1 = 0
sum2 = 0
for i in range(n):
    a = list(map(int,input().split()))
    res = 0
    ans = 0
    flag = False
    for i in range(0,2*t,2):
        x,y = a[i],a[i+1]
        if check(x,y):
            ans += 1
            flag = True
            res = max(res,ans)
        else:
            ans = 0
    if flag:
        sum1 += 1
    if res >= k:
        sum2 += 1
print(sum1)
print(sum2)