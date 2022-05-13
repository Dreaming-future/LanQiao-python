
# 得到1~N的和
def getsum(n):
    return n*(n+1)//2
# [1],[1,2],[1,2,3],[1,2,3,4]....
def getsum2(n):
    '''普通求和方法
    ans = 0
    x = n
    for i in range(1,x+1):
        ans += n*i
        n = n - 1
    return ans
    '''
    # 实际上我们是对 (n*n + n)/2 进行一个求和
    # 这里可以利用小学二年级学的n的平方的求和公式进行加和求解
    #  n平方的求和公式是n (n+1) (2n+1)/6, n 的求和是n(n+1)/2
    return n*(n+1)*(n+2)//6

import math
# 求第N个数在123数列中第几个数列的第几个 求解二次方程 (x^2+x)/2<=N
def findPosition(n):
    if n == 0:
        return (0, 0)
    m = math.floor((math.sqrt(8*n + 1)-1) / 2) # 求根
    c = (m*m+m) // 2
    if n == c:
        return (m, m)
    else:
        return (m + 1, n - c )

t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    (l1,l2) = findPosition(l-1) # l-1个数字在l1的第l2项
    (r1,r2) = findPosition(r) # r个数字在r1的第r2项
    res = getsum2(r1-1) + getsum(r2) - getsum2(l1-1) - getsum(l2)
    print(res)