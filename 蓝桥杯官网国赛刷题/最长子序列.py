sStr = input()
tStr = input()

def getAns(sStr,tStr):
    ans = 0
    for i in tStr:
        if i in sStr:
            ans +=1
            sStr = sStr[sStr.index(i)+1:]

        else:
            return ans
    return ans
print(getAns(sStr,tStr))