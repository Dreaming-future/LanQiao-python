
n = int(input())
m = int(input())
ls = list()

# 构建矩阵存储,链式存储的好处在于能够一次遍历完，矩阵存储的好处是可以直接访问
nex = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    x, y = input().split()
    x = int(x)
    y = int(y)
    nex[x][y] = 1
    nex[y][x] = 1
    
# 最优房间数
leastrooms = n

# i, j存放i房间的第j人编号
roomsets = [[0 for _ in range(n+1)] for _ in range(n)]

# 房间里 人的总数
personnum = [0 for _ in range(n)]

# 思路：无向图染色问题，相邻结点不能染相同颜色。
# 考虑用dfs还是bfs首先考虑划分结点的依据，这题是将人放入不同的房间，这就需要确定房间数。
# 用dfs，将人一个个放入房间，此时只要有解就行，而不需要最优解。总体的框架其实是一个每层单结点的bfs
# 第一个深度是一个房间，第二个是两个房间，而实际上要判断每层是否到达结果还是用的dfs。
# 所以这题还是用的dfs
# 思路:若考场不够，则一个个增加考场，深度有限，可以dfs
# 总结：不一定要用set来加快，增加很删除不如一开始就分配好所有空间。

# dfs返回针对当前对第1..cur-1个人的安排至少需要多少个房间
def dfs(cur, rooms):
    global roomsets, n, leastrooms
    if cur > n:
        leastrooms = min(leastrooms, rooms)
        return
    elif rooms >= leastrooms:
        return
    else:
        # 将cur逐个放入房间i中,并记录最优房间数量
        for i in range(rooms):
            # 可以放入
            num = personnum[i]
            k = 0
            for j in range(1, num+1):
                if not nex[cur][roomsets[i][j]]:
                    k += 1
            if k == num:
                # 加入
                personnum[i] += 1
                roomsets[i][personnum[i]] = cur
                dfs(cur+1, rooms)
                # 恢复
                personnum[i] -= 1

        # 放入空房间
        i += 1
        personnum[i] += 1
        roomsets[i][personnum[i]] = cur
        dfs(cur+1, rooms+1)
        # 恢复
        personnum[i] -= 1
        return


dfs(1, 1)
print(int(leastrooms))


