'''
思路
分输入、判断和输出三个部分
判断部分，逐行逐列遍历每一个元素，
如果是0就进行统计周围的地雷数量，如果非0就把结果列表的该位置置为9
在统计周围的地雷数量时，遍历该位置的四周，即行从i-1到i+1，列从j-1到j+1
如果是1就计数，最后把计数结果放到结果列表中

'''
# 输入
n, m = map(int, input().split())
list = [[0 for _ in range(m)] for _ in range(n)]
ans = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    list[i] = [int(x) for x in input().split()]
    
# 判断
for i in range(n):
    for j in range(m):
        # 逐行逐列判断每一个元素
        if list[i][j] == 0:
            count = 0
            # 判断（i，j）位置元素的四周，即行从i-1到i+1，列从j-1到j+1
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    # (x,y)合法判断：
                    if 0 <= x < n and 0 <= y < m:
                        if list[x][y] == 1:
                            count += 1
            ans[i][j] = count
                    
        else:
            ans[i][j] = 9

# 输出
for i in range(n):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()