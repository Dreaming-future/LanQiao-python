 
def computeD(fn, d):
    (x, y, r) = exGCD(fn, d)
   
    if y < 0:
        return fn + y
    return y
 
def exGCD(a, b):
 
    if b == 0:
        return (1, 0, a)
  
    x1 = 1
    y1 = 0
 
    x2 = 0
    y2 = 1
    while b != 0:
        q = a / b
    
        r = a % b
        a = b
        b = r
   
        x = x1 - q*x2
        x1 = x2
        x2 = x
   
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return(x1, y1, a)
 
p = 891234941
q = 1123984201
d = 212353
 
sum = (p - 1) * (q - 1)
 
e = computeD(sum, d)
print(e)