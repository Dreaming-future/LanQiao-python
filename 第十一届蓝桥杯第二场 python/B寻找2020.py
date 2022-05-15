import os, sys
os.chdir(sys.path[0])

file = open('./2020.txt','r')
lines = file.readlines()
ans = 0
# 直的2020
for line in lines:
    l = len(line)
    for i in range(l-3):
        if line[i:i+4] == '2020':
            ans += 1
# 竖的2020
n,m = len(lines),len(lines[0])

for i in range(n-3):
    for j in range(m):
        if lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j] == '2020':
            ans += 1
# 斜的2020
for i in range(n-3):
    for j in range(m-3):
        if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] == '2020':
            ans += 1
            
print(ans)