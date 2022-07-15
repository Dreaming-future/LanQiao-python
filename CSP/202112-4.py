# http://118.190.20.162/view.page?gpid=T135

n,m,k = map(int,input().split())

class node:
    def __init__(self):
        self.id = 0 # 当前占用的程序id
        self.data = 0 # 程序的数据
        
D = [node() for i in range(m+1)]
for i in range(k):
    a = list(map(int,input().split()))
    c = a[0]
    if a[0] == 0: # 代表写入
        idn,l,r,x = a[1:]
        index,f = 0,0
        for j in range(l,r+1):
            if D[j].id <= 0 or D[j].id == idn:
                D[j].id = idn
                D[j].data = x
                f = 1
                index = j
            else:
                break
        if f == 1:
            print(index)
        else:
            print(-1)
    elif a[0] == 1:
        flag = True
        idn,l,r = a[1:]
        for j in range(l,r+1):
            if D[j].id != idn:
                flag = False
                break         
        if not flag:
            print('FAIL')
        else:
            print('OK')
            for j in range(l,r+1):
                D[j].id = -idn
    elif a[0] == 2:
        flag = True
        idn,l,r = a[1:]
        for j in range(l,r+1):
            if D[j].id != -idn:
                flag = False
                break         
        if not flag:
            print('FAIL')
        else:
            print('OK')
            for j in range(l,r+1):
                D[j].id = idn
    elif a[0] == 3: # 尝试读取
        p = a[1]
        if D[p].id <= 0:
            print('0 0')
        else:
            print(D[p].id,D[p].data)