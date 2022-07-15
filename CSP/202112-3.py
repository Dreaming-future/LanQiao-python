w,s = map(int,input().split())
S = list(input())

# mode = 0 代表大写模式
# mode = 1 代表小写模式 小写转大写需要数字模式过渡
# mode = 2 代表数字模式
def get_mode(x):
    if x.isupper(): return 0
    elif x.islower(): return 1
    elif x.isdigit(): return 2

def change(x):
    '''
    :param x: 当前的数
    :param m: 当前模式
    :return: 返回一个列表，代表转化的过程
    '''
    global mode
    y = get_mode(x)
    a = []
    if mode == y: # 模式相同不用操作
        pass
    else:
        if mode == 0:
            if y == 1:
                a.append(27) # 大写转小写
            elif y == 2:
                a.append(28) # 大写转数字
        elif mode == 2:
            if y == 0:a.append(28) # 数字转大写
            elif y == 1:a.append(27) # 数字转小写
        elif mode == 1: # 小写模式
            a.append(28) # 小写转数字
            if y == 0: # 如果需要转大写0
                a.append(28) # 数字转大写
    mode = y
    if y == 0:
        a.append(ord(x) - ord('A'))
    elif y == 1:
        a.append(ord(x) - ord('a'))
    elif y == 2:
        a.append(int(x) - 0)
    return a

mode = 0
a = []
for i in S:
    a += change(i)

if len(a)%2 == 1:
    a.append(29)
# print(a)
A = []
for i in range(0,len(a),2):
    ans = a[i]*30 + a[i+1]
    A.append(ans)
L = len(A)

if s == -1:
    ans = L + 1 # 全部的码字数量
    x = ans%w
    if x != 0:
        A = A + [900]*(w-x)
    n = len(A) + 1
    print(n)
    for x in A:
        print(x)
else:
    k = pow(2,s+1) # 如果需要校验码
    ans = L + 1 + k
    x = ans%w
    if x != 0:
        A = A + [900]*(w-x)
    r = len(A)
    n = r + 1
    
    # caluate d(x)
    d = [0 for i in range(r+k+1)]
    d[0] = n
    for i in range(r):
        d[i+1] = A[i]
    mod = 929    
    # caluate g(x)
    g = [0 for _ in range(k+1)]
    g[0] = 1
    a = -3
    # i 为第几次项
    for i in range(1,k+1):
        for j in range(i-1,-1,-1):
            g[j+1] = (g[j+1] + g[j]*a)%mod # 模拟计算
        a = a*3
    # 模拟除法
    for i in range(r+1):
        x = d[i]
        d[i] = 0
        for j in range(1,k+1):
            d[i+j]  = (d[i+j] - x*g[j])%mod # 取mod计算更快
            
    print(n)
    for x in A:
        print(x)
    
    for i in range(r+1,r+k+1):
        print(-d[i]%mod)