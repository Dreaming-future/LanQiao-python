
n = int(input())

s = set()
ans = 1
for i in range(n):
    a,b = map(int,input().split())
    if (a,b) not in s:
        s.add((a,b))

s = list(s)
crosspoint_x_set = set()
each_line_num = [1]*(len(s)+1)
for i in range(1,len(s)):
    crosspoint_x_set.clear()
    for j in range(i):
        if s[i-j-1][0] != s[i][0]:
            x = (s[i][1]-s[i-j-1][1]) / (s[i-j-1][0] - s[i][0])
            crosspoint_x_set.add(x)
    each_line_num[i] += len(crosspoint_x_set)
print(sum(each_line_num))