
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return True
    return False

ans = 0
for i in range(1,2020 + 1):
    if prime(i):
        ans += 1
print(ans)