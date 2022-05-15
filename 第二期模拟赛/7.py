a,b,c = map(int,input().split())


a,b,c = sorted([a,b,c])
if a*a + b*b == c*c:
    print('YES')
else:
    print('NO')
