import os
import sys

# 请在此输入您的代码

n,t = map(int,input().split())
s = input()

def C(x):
    x = list(map(int,x))
    s = [x[0]]
    for i in range(1,len(x)):
        s.append(x[i-1]^x[i])
    s = ''.join(map(str,s))
    return s

c = 1
while c < n:
    c <<= 1
t %= c
for _ in range(t):
    s = C(s)
    # print(s)
  
print(s)