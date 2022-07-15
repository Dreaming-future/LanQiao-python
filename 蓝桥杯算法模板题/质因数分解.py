

n = 100
from math import sqrt
for i in range(2,int(sqrt(n))+1):
    while n % i == 0:
        print(i,end=' ')
        n //= i
