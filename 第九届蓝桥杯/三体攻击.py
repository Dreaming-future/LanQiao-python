# https://www.lanqiao.cn/problems/180/learning/
import os
import sys


A,B,C,m = map(int,input().split())
# 战舰生命值列表
life = list(map(int,input().split()))
# 战舰生命值与编号映射
d = {}
for i in range(1,A+1):
  for j in range(1,B+1):
    for k in range(1,C+1):
      d[(i,j,k)] = life[((i-1)*B + (j-1))*C + (k-1)]

flag = False
for i in range(1,m+1):
  li,ri,lj,rj,lk,rk,ht = map(int,input().split())
  for key in d.keys():
    if li <= key[0] <= ri and lj <= key[1] <= rj and lk <= key[2] <= rk:
      d[key] -= ht
      if d[key] < 0:
        print(i)
        flag = True
        break
  if flag:
    break