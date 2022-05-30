

import datetime
y,m,d = map(int,input().split())

d = datetime.date(y,m,d)
print(d.isoweekday())