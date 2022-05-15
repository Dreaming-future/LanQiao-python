import os
import sys

# 请在此输入您的代码

a = ['UDDLUULRUL',
'UURLLLRRRU',
'RRUURLDLRD',
'RUDDDDUUUU',
'URUDLLRRUU',
'DURLRLDLRL',
'ULLURLLRDU',
'RDLULLRDDD',
'UUDDUDUDLL',
'ULRDLUURRR']
# a = ['ULDL','RRUL','LRDL','ULLR']

cnt = 0
def dfs(i,j):
  if i < 0 or i > 9 or j < 0 or j > 9:
    global cnt
    cnt += 1
    return 
  if vis[i][j] == 1:
    return 
  vis[i][j] = 1
  if a[i][j] == 'U':
    return dfs(i - 1,j)
  elif a[i][j] == 'D':
    return dfs(i + 1,j)
  elif a[i][j] == 'L':
    return dfs(i,j-1)
  elif a[i][j] == 'R':
    return dfs(i,j+1)
  
for i in range(10):
  for j in range(10):
    vis = [[0]*10 for _ in range(10)]
    dfs(i,j)
print(cnt)


# vis = [[0]*10 for _ in range(10)]
# ans = [[False]*10 for _ in range(10)]
# cnt = 0
# for i in range(10):
#   for j in range(10):
#     x,y = i,j
#     s = []
    
#     while vis[x][y] == 0:
#       vis[x][y] = 1
#       s.append([x,y])
#       if a[x][y] == 'U':
#         x -= 1
#       elif a[x][y] == 'D':
#         x += 1
#       elif a[x][y] == 'L':
#         y -= 1
#       elif a[x][y] == 'R':
#         y += 1
      
#       if x < 0 or x > 9 or y < 0 or y > 9 or ans[x][y] == True:
#         for j,k in s:
#           ans[j][k] = True
#           cnt += 1
#         break

# print(cnt)