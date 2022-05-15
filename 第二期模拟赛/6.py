
p,t = map(int,input().split())

if t % 12==0:
    print(p*(t//12))
else:
    print(p*(t//12+1))
