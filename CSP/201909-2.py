# http://118.190.20.162/view.page?gpid=T93

n = int(input())

T,D,E = 0,0,0
ans = 0
flag1, flag2 = False, False
for j in range(n):
    x = list(map(int,input().split()))
    m, a = x[0], x[1:]
    c = a[0]
    flag = False
    for i in range(1,m):
        if a[i] > 0:
            if c != a[i]:
                flag = True
                c = a[i]
        elif a[i] <= 0:
            c += a[i]
    if flag:
        D += 1
        ans += 1
        if j <= 1:
            if j == 0:
                flag1 = True
            elif j == 1:
                flag2 = True
    else:
        ans = 0
    T += c # 统计车辆
    
    # 如果连续三个一起，就 E+=1
    if ans == 3:
        ans -= 1
        E += 1
    # 判断循环的1和2
    if j == n - 1: # 到了倒数第二个的时候
        if ans == 2:
            if flag1:
                E += 1
            if flag2:
                E += 1


print(T,D,E)