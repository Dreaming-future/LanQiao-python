def bubble (words):
    count = 0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]
                count += 1
    return count

print(bubble(list('onmlkjihgfedcba')))
print(bubble(list('jonmlkihgfedcba')))

import os
import sys

# 请在此输入您的代码
'''
条件
 最短字符串 条件1
 最小字典序 条件2
 100次交换 条件3
完全逆序交换次数  jh = n*(n-1)/2
字符串长度为15时  jh=105
所以最短字符串长度就是15
条件1 已满足
最小字典序，从a开始，到o
条件2 已满足
完全逆序是 o~a
少交换5次。只需要把第6位的数，往前交换五次，排在首位
相应就是 只交换100次
'''
print('jonmlkihgfedcba')