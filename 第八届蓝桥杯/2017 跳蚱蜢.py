import os
import sys
import time
# 请在此输入您的代码
x = time.time()
start = '012345678'
end = '087654321'

import collections
q = collections.deque([])

q.append([start,0])
s = set()
s.add(start)
while q:
    node = q.popleft()
    step = node[1]
    node = node[0]
    if node == end:
        break
    pos = node.index('0')
    posi = [0]*4
    posi[0] = (pos+1)%9
    posi[1] = (pos+2)%9
    posi[2] = (pos+8)%9
    posi[3] = (pos+7)%9
    for i in range(4):
        # node_list = list(node)
        # newnode = node[posi[i]] + node[node[pos[i]]
        # node_list[pos] = node_list[posi[i]]
        # node_list[posi[i]] = '0'
        # node_list = ''.join(node_list)
        if pos <  posi[i]:
            new_node = node[:pos] +  node[posi[i]] + node[pos+1:posi[i]] + node[pos] + node[posi[i]+1:]    
        else:
            new_node = node[:posi[i]] + node[pos] + node[posi[i]+1:pos] + node[posi[i]] + node[pos+1:]
        if new_node not in s:
            s.add(new_node)
            q.append([new_node,step+1])

print(step)
y = time.time()
print(y-x)