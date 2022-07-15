
# http://118.190.20.162/view.page?gpid=T88

n = int(input())

for i in range(n):
    s = input()
    s = s.replace('/', '//').replace('x', '*')
    res = eval(s)
    if res == 24:
        print('Yes')
    else:
        print('No')
