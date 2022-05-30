
n,X,Y = map(int,input().split())

def dist(x1,y1,x2,y2):
    
    return (x1-x2)**2+(y1-y2)**2

l = {}
for i in range(n):
    x,y = map(int,input().split())
    l[i] = dist(X,Y,x,y)
# print(l)

# sorted(l.keys(), keys = lambda x:x.keys())
l = sorted(l.items(),key=lambda x:x[1])

# print(l)
# print(l[:3])
print('\n'.join(str(i[0]+1) for i in l[:3]))