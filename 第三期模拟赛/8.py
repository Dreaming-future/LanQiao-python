import datetime

s = input()
e = input()

def change(x):
    x = x.split(':')

    date = datetime.datetime(2022,4,8,hour=int(x[0]),minute=int(x[1]),second=int(x[2]))
    return date

s = change(s)
e = change(e)
print(e-s)
