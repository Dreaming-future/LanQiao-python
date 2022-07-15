
n,a,b = map(int,input().split())

d1,d2 = {},{}
for i in range(a):
    index,value = map(int,input().split())
    d1[index] = value

for i in range(b):
    index,value = map(int,input().split())
    d2[index] = value
    
ans = 0
for k,v in d1.items():
    if k in d2:
        ans += v * d2[k]
print(ans)