
n = int(input())

s = set()
for i in range(n):
    x,y = map(int,input().split())
    s.add((x,y))

f = [(1,0),(-1,0),(0,1),(0,-1)]
f2 = [(1,1),(-1,1),(1,-1),(-1,-1)]
def check(x,y):
    for i,j in f:
        xi,yi = x+i,y+j
        if (xi,yi) not in s:
            return False,0
    res = 0
    for i,j in f2:
        xi,yi = x+i,y+j
        if (xi,yi) in s:
            res += 1
    return True,res
a = list(s)
from collections import defaultdict
score = defaultdict(int)
for i,j in a:
    flag,ans  = check(i,j)
    if flag:
        score[ans] += 1
for i in range(5):
    print(score[i])