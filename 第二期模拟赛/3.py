s = set()
for i in range(1012):
    for j in range(i+1,1012):
        x = j*j - i*i
        if x not in s and 1<=x<=2021:
            s.add(x)
print(len(s)) # 答案：1516
##print(s)
