"""
https://www.lanqiao.cn/problems/1244/learning/
难度: 简单   标签: 威尔逊定理
"""

n = int(input())

flag = False
for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        flag = True
        break

if not flag:
    print(n-1)
else:
    if n == 4:
        print(2)
    else:
        print(0)
