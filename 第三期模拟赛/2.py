from math import gcd

def g(a,b):
    return a*b//gcd(a,b)

cnt = 0
for i in range(1,2022):
    if g(i,2021) == 4042:
        cnt += 1
print(cnt) # 答案3
