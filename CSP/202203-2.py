# http://118.190.20.162/view.page?gpid=T142

n,m,k = map(int,input().split())

N = 200010
diff = [0]*N 
for i in range(n):
    t,c = map(int,input().split())
    # 在【l, r】时间段内做核酸，则t时刻可进入
    l = max(t-k-c+1,0)
    r = max(t-k,0)
    # 在【l, r】时间段内能出行的计划个数加一
    diff[l] += 1
    diff[r+1] -= 1
# 利用差分计算每个时间的能出行个数
for i in range(1,N):
    diff[i] += diff[i-1]
for j in range(m):
    q = int(input())
    res = diff[q]
    print(res)