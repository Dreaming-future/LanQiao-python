
s = 'tocyjkdzcieoiodfpbgcncsrjbhmugdnojjddhllnofawllbhfiadgdcdjstemphmnjihecoapdjjrprrqnhgccevdarufmliqijgihhfgdcmxvicfauachlifhafpdccfseflcdgjncadfclvfmadvrnaaahahndsikzssoywakgnfjjaihtniptwoulxbaeqkqhfwl'
# s = 'lanqiao'
n = len(s)
h = set()

def add(x):
    if x not in h:
        h.add(x)

def dfs(i,tmp):
    add(tmp)
    for j in range(i+1,n):
        if ord(s[j]) > ord(tmp[-1]):
            tmp += s[j]
            if tmp not in h:
                dfs(j,tmp)
            tmp = tmp[:-1]

for i in range(n):
    if s[i] not in h:
        dfs(i,s[i])
print(len(h))

print(3616159)

# 动态规划
str1 = 'tocyjkdzcieoiodfpbgcncsrjbhmugdnojjddhllnofawllbhfiadgdcdjstemphmnjihecoapdjjrprrqnhgccevdarufmliqijgihhfgdcmxvicfauachlifhafpdccfseflcdgjncadfclvfmadvrnaaahahndsikzssoywakgnfjjaihtniptwoulxbaeqkqhfwl'
lst = [1]*len(str1)
for i in range(len(str1)):
    for z in range(i):
        if str1[z] < str1[i]:
            lst[i] += lst[z]
        elif str1[z] == str1[i]:
            lst[i] -= lst[z]
print(sum(lst))
