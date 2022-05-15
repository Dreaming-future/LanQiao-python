
n = int(input())
grade = []
a = 0
b = 0
for i in range(n):
    grade.append(int(input()))
    if grade[i] >= 85:
        a += 1
        b += 1
    elif grade[i] >= 60:
        b += 1
print('{:2.0f}%'.format(b/n*100))
print('{:2.0f}%'.format(a/n*100))