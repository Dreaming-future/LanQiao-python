
import datetime

start = datetime.date(2000, 1, 1)
end = datetime.date(2020,10,1)

ans = 0
while start != end:
    if start.isoweekday() == 1 or start.day == 1:
        ans += 1
    ans += 1
    start += datetime.timedelta(days=1)
# 还有最后一天
print(ans+2)