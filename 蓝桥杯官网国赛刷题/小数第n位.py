a,b,n = map(int,input().split())


def qpow(a,b,mod):
    ans = 1
    while b:
        if b&1:
            ans = ans*a%mod
        a = a*a%mod
        b = b>>1
    return ans
mod = 1000*b
x = a*qpow(10,n+2,mod)%mod//b
print("%03d"%x)