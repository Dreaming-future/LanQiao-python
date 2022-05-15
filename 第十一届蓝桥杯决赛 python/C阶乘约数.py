
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return True
    return False

l = [i for i in range(2,100+1) if not prime(i)]

cnt = [0]*len(l)
for i in range(2,101):
    for j in range(len(l)):
        x = l[j]
        k = i
        while k%x == 0:
            cnt[j] += 1
            k = k // x
ans = 1
for x in cnt:
    ans *=(x+1)
print(ans)