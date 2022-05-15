import os
import sys
import datetime

idate = input()
y = int(idate[:4])
m = int(idate[4:6])
d = int(idate[6:])
dd = datetime.date(y,m,d) # 将y,m，d转化为日期格式
flag = True # 输出一次回文日期
for i in range(9999999):
    dd += datetime.timedelta(days=1) # +1天
    s = str(dd).replace('-','')
    if s == s[::-1]:
        if flag:
            print(s)
            flag = False
        if s[0] == s[2] == s[-1] == s[-3] and s[1] == s[3] == s[-2] == s[-4]:
            print(s)
            break
