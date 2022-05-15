
class TimeCost():
    def __init__(self,s,a,e):
        self.w = s + a
        self.s = self.w + e
    # 按照规则排序
    def __lt__(s, o):
        return s.s < o.s

n = int(input())
l = []
for i in range(n):
    s,a,e = map(int,input().split())
    l.append(TimeCost(s,a,e))

l = sorted(l) # 就按照时间和排序一下就行了
ans = 0
ans2 = 0
for i in l:
    ans += i.w + ans2
    ans2 += i.s
print(ans)