
s = input()
sub = ''
person = []
for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        if sub != '':
            person.append(sub)
        sub = s[i]
    else:
        sub += s[i]
person.append(sub)
# print(person)
n = len(person)
dp = [1]*n
from collections import defaultdict
Index = defaultdict()
for i in range(n):
    Index[i] = person[i]
    
    
MAX = 0
MAX_STR = 'Z'
for i in range(n):
    for j in range(i+1,n):
        if person[j] > person[i]:
            if dp[i] + 1 >= dp[j]:
                dp[j] = dp[i] + 1
                Index[j] = Index[i] + person[j]
            
            if dp[j] == MAX and MAX_STR > Index[j]:
                MAX_STR = Index[j]
            
            if dp[j] > MAX:
                MAX = dp[j]
                MAX_STR = Index[j]

# print(Index)
# maxindex = dp.index(max(dp))
# print(person)
# print(dp)
# print(Index[maxindex])
print(MAX_STR)