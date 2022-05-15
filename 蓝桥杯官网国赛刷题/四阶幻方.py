alist = [i for i in range(17)]
used = [0 for _ in range(17)]
tube = [0 for _ in range(17)]
ans = 0
def dfs(pos):
    if pos == 17:
        if tube[1] + tube[6] + tube[11]+ tube[16]==34:
            global ans
            ans+=1
            return
    elif pos == 5:
        if tube[1] + tube[2] + tube[3]+ tube[4] != 34:
            return
    elif pos == 9:
        if tube[5] + tube[6] + tube[7]+ tube[8] != 34:
            return
    elif pos == 13:
        if tube[9] + tube[10] + tube[11]+ tube[12] != 34:
            return
    elif pos == 14:
        if tube[4] + tube[7] + tube[10]+ tube[13] != 34 or tube[1] + tube[5] + tube[9]+ tube[13] != 34:
            return
    elif pos == 15:
        if tube[2] + tube[6] + tube[10]+ tube[14] != 34:
            return
    elif pos == 16:
        if tube[3] + tube[7] + tube[11]+ tube[15] != 34:
            return
    for i in range(1,17):
        if not used[i]:
            tube[pos] = alist[i]
            used[i] = 1
            dfs(pos+1)
            used[i] = 0
tube[1] = 1
used[1] = 1
dfs(2)
print(ans)