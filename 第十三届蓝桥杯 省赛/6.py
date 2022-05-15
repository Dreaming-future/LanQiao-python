
s = input()

def f(x):
    s = set()
    for i in range(1,len(x)-1):
        if (x[i] == x[i-1] and x[i] != x[i+1]):
            s.add(i)
            s.add(i+1)
        elif (x[i] != x[i-1] and x[i] == x[i+1]):
            s.add(i-1)
            s.add(i)
    if not s:
        return x,False
    sr = ''
    for i in range(len(x)):
        if i not in s:
            sr += x[i]
    
    return sr,True

for i in range(1<<64):
    s,flag = f(s)
    if s == '':
        print('EMPTY')
        break
    elif flag == False:
        print(s)
        break
