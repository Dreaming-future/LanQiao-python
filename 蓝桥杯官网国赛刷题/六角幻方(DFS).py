def dfs(pos):
    if pos == 20:
        if a[17] + a[18] + a[19] == a[3] + 15 + 13 and a[12] + a[16] + a[19] == a[3] + 15 + 13 and a[1] + a[5] + a[10] + a[15] + a[19] == a[3] + 15 + 13:
            print(a[8],a[9],a[10],a[11],a[12])
            exit(0)
    elif pos == 8:
        if a[4] + a[5] + a[6] + a[7] != a[3] + 15 + 13:
            return
    elif pos == 9:
        if a[1] + a[4] + a[8] != a[3] + 15 + 13:
            return
    elif pos == 13:
        if a[8] + a[9] + a[10] +a[11] + a[12] != a[3] + 15 + 13 or a[3] + a[7] + a[12] != a[3] + 15 + 13:
            return 
    elif pos == 14:
        if a[2] + a[5] + a[9] + a[13] != a[3] + 15 + 13:
            return
    elif pos == 17:
        if a[13] + a[14] + a[15] + a[16] != a[3] + 15 + 13 or a[2] + a[6] + a[11] + a[16] != a[3] + 15 + 13:
            return
    elif pos == 18:
        if a[3] + a[6] + a[10] + a[14] + a[17] != a[3] + 15 + 13 or a[8] + a[13] + a[17] != a[3] + 15 + 13:
            return
    elif pos == 19:
        if a[4] + a[9] + a[14] + a[18] != a[3] + 15 + 13 or a[7] + a[11] + a[15] + a[18] != a[3] + 15 + 13:
            return
    for i in range(1,20):
        if not used[i]:
            used[i] = 1
            a[pos] = i
            dfs(pos+1)
            used[i] = 0

used = [0]*20
a = [0]*(20)
used[13] = 1
used[15] = 1
a[1] = 15
a[2] = 13
dfs(3)