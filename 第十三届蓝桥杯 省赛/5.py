
import math
d1,p1,q1,d2,p2,q2 = map(int,input().split())

x = (d1,p1,q1)
y = (d2,p2,q2)


def getxy(d,p,q):
    x,y =0,0
    if d == 0:
        x -= p
        
        x += q//2
        if q%2 == 0:
            x -= 1
        y += q
    elif d == 1:
        x -= p//2
        y += p
        
        x += q
    elif d == 2:
        y += p
        x += p//2
        
        y -= q
        x += q//2
    elif d == 3:
        x += p
        
        x -= q//2
        y -= q
    elif d == 4:
        y -= p
        x += p//2
        
        x -= q
    elif d == 5:
        y -= p
        x -= p//2
        
        x -= q//2
        y += q

    return x,y

x1,y1 = getxy(d1,p1,q1)
x2,y2 = getxy(d2,p2,q2)
print(x1,y1,x2,y2)
def dist(x1,y1,x2,y2):
    ans = abs(x1-x2)
    if abs(y1-y2)%2 == 0:
        ans += 1
    return ans
print(dist(x1,y1,x2,y2))
