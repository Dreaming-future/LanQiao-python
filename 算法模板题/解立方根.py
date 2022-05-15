'''
https://www.lanqiao.cn/problems/1217/learning/
'''

t = int(input())
eps = 1e-5
for _ in range(t):
    n = int(input())
    l = 0
    r = 100000
    while l <= r:
        mid = (l + r)//2 + 1
        if abs(mid**3 - n) <= eps:
            res = mid
            break
        elif abs(mid**3 - n) > 0:
            r = mid - 0.0001
        else:
            l = mid + 0.0001
    print("%.2f"%res)
