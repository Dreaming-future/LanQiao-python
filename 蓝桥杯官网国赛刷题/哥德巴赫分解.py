

def get_prime(x):
    prime = [1]*(x+1)
    prime[0] = prime[1] = 0
    for i in range(2,int(x**0.5)+1):
        if prime[i] == 1:
            for j in range(i+i,x+1,i):
                prime[j] = 0
    return prime

n = 10000
prime = get_prime(n)
a = []
for i in range(2,n+1):
    if prime[i] == 1:
        a.append(i)

number = 0        
n = 4
s = set()
while n <= 10000:
    for i in range(len(a)):
        if n-a[i] <= a[i]: break
        if n - a[i] in a:
            number = max(number,min(a[i],n-a[i]))
            break
    n += 2
print(number)