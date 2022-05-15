s = input()

for i in range(len(s)-1,0,-1):
    if s[i] > s[i-1]:
        flag = True
    else:
        flag = False
        break
if not flag:
    print('NO')
else:
    print('YES')
