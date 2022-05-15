
def find(x):
    if x!=f[x]:
        f[x] = find(f[x])
    return f[x]
def union(x,y):
    fx,fy = find(x),find(y)
    if fx!=fy:
        f[fx] = fy

n = int(input())
f = [i for i in range(n+1)]
a = map(int,input().split())
for i,v in enumerate(a):
    union(i+1,v)

s = set()
for i in range(1,n+1):
    x = find(i)
    if x not in s:
        s.add(x)
print(len(s))
