n,N = map(int,input().split())
a = list(map(int,input().split()))
s = 0
# print(a)
for i in range(1,n):
    s += (a[i] - a[i-1]) * i
s += (N - a[n-1])*n
print(s)