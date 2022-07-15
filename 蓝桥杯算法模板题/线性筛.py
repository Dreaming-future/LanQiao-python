
# # 线性筛
# n = 100
# isprime = [False]*(n+1)
# prime = [0]*(n+1)
# cnt = 0
# for i in range(2,n+1):
#     if isprime[i] == False:
#         prime[cnt] = i
#         cnt += 1
#     for j in range(cnt):
#         if i*prime[j] > n: break # 超出范围，break
#         isprime[i*prime[j]] = True # 为倍数的设为true
#         if i%prime[j] == 0: break # 

# print(prime)


n = int(input())
isprime = [False]*(n+1)
primes = [0]*(n+1)

cnt = 0
for i in range(2,n+1):
    if not isprime[i]:
        primes[cnt] = i
        cnt += 1
        
    for j in range(cnt):
        if i*primes[j] > n: break
        isprime[i*primes[j]] = True
        if i%primes[j] == 0: break
print(cnt)