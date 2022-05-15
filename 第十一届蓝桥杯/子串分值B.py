# # 100分
# list1=list(input())
# list2=[-1 for i in range(26)]
# count=0

# for i in range(len(list1)):
#     index=ord(list1[i])-ord('a')
#     count+=(len(list1)-i)*(i-list2[index])
#     list2[index]=i

# print(count)
s = input()
l = [-1]*26
n = len(s)
ans = 0
for i in range(n):
    index = ord(s[i]) - ord('a')
    ans += (n-i)*(i-l[index]) # 从上一次出现到末尾的位置，都有此字符，并且各个位置组合得
    l[index] = i # 记录上一次出现位置
print(ans)