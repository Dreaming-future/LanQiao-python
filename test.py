
from itertools import permutations as p
n = [1,2,3,4,5,7,8,9,10,12,13]


for x in p(n):
    a = x[0] + x[1] + x[2] + x[3]
    b = 6 + x[1] + x[4] + 14
    c = 6 + x[2] + x[5] + 11
    d = x[3] + x[5] + x[8] + x[10]
    e = x[0] + x[4] + x[6] + x[9]
    f = x[7] + x[8] + x[9] + 11
    g = 14 + x[6] + x[7] + x[10]
    if a == b == c == d == e == f == g:
          print(x[0],x[1],x[2],x[3])
          break
    