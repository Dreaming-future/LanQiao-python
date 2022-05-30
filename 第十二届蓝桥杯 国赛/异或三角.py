
import sys
sys.setrecursionlimit(1<<31-1)
N = 32
f = [[[[[[[-1]*2 for _ in range(2)] for _ in range(2)] for _ in range(2)]for _ in range(2)] for _ in range(2)] for _ in range(N)]
a = [0]*N
def dfs(pos, op1, op2, op3, c1, c2, big):
    if not pos: return big and c1 and c2
    # 如果不是-1的话，也就是计算过，记忆化搜索
    if ~f[pos][op1][op2][op3][c1][c2][big]:
        return f[pos][op1][op2][op3][c1][c2][big]

    up1 = a[pos] if op1 else 1
    up2 = a[pos] if op2 else 1
    up3 = a[pos] if op3 else 1
    res = 0
    res += dfs(pos-1,op1 and (not up1),op2 and (not up2),op3 and (not up3),c1,c2,big)
    if up1 and up3:
        res+=dfs(pos-1,op1,op2 and (up2==0),op3,c1,1,big);
    if up2 and up3:
        res+=dfs(pos-1,op1 and (up1==0),op2,op3,1,c2,big);
    if c1 and c2:
        res+=dfs(pos-1,op1,op2,op3 and (not up3),1,1,1)
    f[pos][op1][op2][op3][c1][c2][big] = res
    return f[pos][op1][op2][op3][c1][c2][big]

def solve(x):
    pos = 0
    # 把数拆分至a数组中
    for i in range(N):
        for j in range(2):
            for k in range(2):
                for b in range(2):
                    for c in range(2):
                        for d in range(2):
                            for e in range(2):
                                f[i][j][k][b][c][d][e] = -1
    
    while x:
        pos += 1
        a[pos] = x%2 # x % 进制
        x = x//2 # x / 进制
    # 从最高位开始枚举，刚开始默认为有限制
    return dfs(pos,1,1,1,0,0,0)
t = int(input())
for i in range(t):
    n = int(input())
    res = solve(n)*3
    print(res)
