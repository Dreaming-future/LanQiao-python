
import datetime

date1 = input()
date2 = input()
y,m,d = int(date1[:4]),int(date1[4:6]),int(date1[6:])
date1 = datetime.date(y,m,d)

y,m,d = int(date2[:4]),int(date2[4:6]),int(date2[6:])
date2 = datetime.date(y,m,d)

ans = 0
while date1 != date2:
    x = str(date1).split('-')
    x = ''.join(x)
    if x == x[::-1]:
        ans += 1
    date1 += datetime.timedelta(days=1)
x = str(date1).split('-')
x = ''.join(x)
if x == x[::-1]:
    ans += 1
print(ans)