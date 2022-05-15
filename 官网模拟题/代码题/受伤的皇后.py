import os
import sys

n = int(input())

# 检查一下(row,col)位置是否合法
def check(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def queen(board, row):
    border = len(board)
    if row >= border:
        global cnt
        cnt += 1
    col = 0
    for col in range(border):
        if check(board, row, col):
            board[row] = col
            queen(board, row+1)


b = [0]*n
cnt = 0
queen(b, 0)
print(cnt)


# n = int(input())  # 皇后数量
# col = [100]*n  # 记录每一行的皇后在第几列
# count = 0
# def dfs(row):
#     global n,col,count
#     if row == n:
#         count+=1#这是一个递归出口，表示到底了
#         return

#     for i in range(n):#i表示这一行中，皇后放第几列
#         flage = True
#         for k in range(n):
#             if i == col[k]:#col是存第几行存在了第几列
#                 flage = False#首先要判断这个位置能不能放
#             elif abs(row-k)==abs(i-col[k]) and abs(row-k)<3:
#                 flage = False
            
#         if flage:
#             col[row] = i#标记
#             dfs(row+1)#可以放就放了，然后做递归判断下一行
#             col[row] = 100#这里要回溯？因为做完这一行，就返回到上一行去换一列
            
# dfs(0)
# print(count)