
import datetime

s = datetime.date(2000,1,1)
e = datetime.date(2020,10,2)
ans = 0
while s != e:
    if s.isoweekday() == 1 or s.day == 1:
        ans += 1
    ans += 1
    s += datetime.timedelta(days=1)
# 还有最后一天
print(ans)