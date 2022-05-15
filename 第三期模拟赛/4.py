
a = ['0 9 3 0 0 0 0 9',
'9 0 8 1 4 0 0 0',
'3 8 0 9 0 0 0 0',
'0 1 9 0 3 0 0 5',
'0 4 0 3 0 7 0 6',
'0 0 0 0 7 0 5 2',
'0 0 0 0 0 5 0 4',
'9 0 0 5 6 2 4 0']


graph = [[0]*9 for _ in range(9)]

for i in range(8):
    a[i] = a[i].split(' ')
    for j in range(8):
        graph[i+1][j+1] = int(a[i][j])

def find(x):
    if father[x] != x:
        father[x] = find(father[x])
    return father[x]

def union(x,y):
    fx,fy = find(x),find(y)
    if fx!=fy:
        father[fx] = fy

father = [i for i in range(9)]
ans = 0
for x in range(1,8):
    w = float('inf')
    for i in range(1,9):
        for j in range(1,9):
            # 首先有边
            if graph[i][j] != 0 and find(i) != find(j):
                if w > graph[i][j]:
                    w = graph[i][j]
                    a = i
                    b = j
    ans += w
    union(a,b)
    print(a,b,w)
print(ans) # 答案26
