
a = [i*i for i in range(45)]

s = set()
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] + a[j] not in s and 1 <= a[i] + a[j] <= 2021:
            s.add(a[i]+a[j])
# print(s)
print(len(s)) # 答案 624
