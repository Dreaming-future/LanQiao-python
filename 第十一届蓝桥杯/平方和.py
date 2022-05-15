import os
import sys

# 请在此输入您的代码
n = 2019

ans = 0
for i in range(1,2019+1):
    if '0' in str(i) or '1' in str(i) or '2' in str(i) or '9' in str(i):
        ans += i*i
print(ans)