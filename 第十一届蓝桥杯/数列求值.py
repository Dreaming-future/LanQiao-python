
n = 20190324
a,b,c = 1,1,1
for i in range(n-3):
    a,b,c = b,c,a+b+c
print(c%10000)