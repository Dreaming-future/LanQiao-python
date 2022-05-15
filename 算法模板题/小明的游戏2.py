"""
https://www.lanqiao.cn/problems/1219/learning/
难度: 简单   标签: 反nim博弈
"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    flag = True
    ans = 0
    cnt = 0
    for x in a:
        if x > 1:
            flag = False
        ans = ans^x
    if flag:
        if ans == 0:
            print('NO') # ans = 0,nim和为0，也就说明是偶数，这时候先手必胜
        else:
            print('YES')
    else:
        if ans != 0: # 至少有一堆>1,并且nim不为0，先手胜
            print('NO')
        else:
            print('YES')
        
