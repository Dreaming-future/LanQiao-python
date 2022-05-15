
import collections
h = collections.Counter() # 哈希表 h = {} h['2'] = 0
for i in range(1,2020+1):
    for x in str(i):
        h[x] += 1

print(h['2'])