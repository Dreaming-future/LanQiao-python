t,a,p = map(int,input().split())

page = t // a

if p <= page:
    print((p-1)*a+1,p*a)
elif p > page:
    if t%a >0:
        x = t % a
        print((p-1)*a+1,(p-1)*a+x)
