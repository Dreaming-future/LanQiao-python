# https://www.lanqiao.cn/problems/595/learning/
import itertools
class UnionFindSet():
    def __init__(self,n):
        self.count = 0 # 当前连通分量数目
        # self.count = n # 不连通区域
        self.father=[x for x in range(n)]
    def find(self,x):
        root = x
        while self.father[root]!=root: # 找根节点
            root=self.father[root]
            
        # 路径压缩
        while x != root:
            o = self.father[x] # 找x的父节点
            self.father[x] = root # 把x的父节点设置成刚才找到的根
            x = o # 往上一层
        return root
    
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x != y:
            self.father[y]=x # 合并
            self.count +=1
        return 0
    
result = 0
nums = [x for x in range(7)]
for x in range(1,8): # 每次用的晶体管个数
    for k in itertools.combinations(nums, x): #从所有的晶体管中按个数要求不重复的拿。
        l = len(k)#晶体管的个数
        ufs = UnionFindSet(l)
        #两两的逐个选取
        for a in range(l):
            for b in range(a+1,l):
                #根据下图的数字判断两个晶体管是否相邻。
                if abs(k[a]-k[b])==1 or (k[a]==1 and k[b]==6) or (k[a]==2 and k[b]==6) or (k[a]==4 and k[b]==6) or (k[a]==0 and k[b]==5):
                    ufs.union(a,b)
        if l-ufs.count==1: #比如当用到三个二极管的时候只需要链接两次，那么当晶体管个数减去链接次数为1的时候符合要求。
            result += 1
print(result)