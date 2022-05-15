
# import collections
# s = input()

# c = collections.Counter(s)
# key,value = c.most_common(1)[0][0],c.most_common(1)[0][1] # 得到出现次数最多的数据，但不一定是最小的
# # 在很多相同的次数的字母中，要寻找字典序最小的
# for item in c.most_common():
#     k,v = item
#     if v < value:
#         break
#     if ord(k) < ord(key):
#         key = k
    
# print(key)
# print(value)


a=input()
dicts={}
for i in a:
    dicts[i]=dicts.get(i,0)+1
l = sorted(dicts.items(), key= lambda x:x[1])
print(l[-1][0])
print(l[-1][1])
