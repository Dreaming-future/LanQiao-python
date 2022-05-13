

def get_prime(n):
    prime = [1]*(n+1)
    prime[0] = 0
    prime[1] = 0
    for i in range(2,int(n**0.5)+1):
        if prime[i] == 1:
            for j in range(2*i,n+1,i):
                prime[j] = 0
    return prime
cnt = 0
n = 20210605
prime = get_prime(n)
##for i in range(n+1):
##    if prime[i]:
##        print(i,end=' ')
for i in range(1,n+1):
    if prime[i]:
        flag = True
        for j in str(i):
            j = int(j)
            if prime[j] == 0:
                flag = False
                break
        if flag:
            cnt += 1

print(cnt)
            
