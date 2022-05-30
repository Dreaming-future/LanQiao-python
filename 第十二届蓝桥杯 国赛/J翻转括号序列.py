# https://www.lanqiao.cn/problems/1589/learning/

n,m = map(int,input().split())
S = input()
A = [0]
# ( 设为1 ) 设为-1
A.extend([1 if s=='(' else -1 for s in S])

class node:
    def __init__(self) -> None:
        self.sum = 0 # 前缀和
        self.max = 0 # 前缀和中的最大值
        self.min = 0 # 前缀和中的最小值
        self.index_min = 0
        self.index_max = 0
        self.tag = 0
        
# create tree
tree = [node() for i in range(n<<2)]

def ls(p):return p << 1
def rs(p):return p << 1|1

def build(p,pl,pr):
    if pl == pr:
        tree[p].sum = tree[p].min =  tree[p].max = A[pl]
        tree[p].index_min = tree[p].index_max = pl
        return
    mid = (pl + pr) >> 1
    build(ls(p),pl,mid)
    build(rs(p),mid+1,pr)
    push_up(p)

# 进行翻转，更改标记
def addtag(p):
    tree[p].tag = 1 - tree[p].tag
    tree[p].sum *= -1
    tree[p].min, tree[p].max = -tree[p].max, -tree[p].min
    tree[p].index_min, tree[p].index_max = tree[p].index_max, tree[p].index_min


def push_down(p):
    if tree[p].tag == 1:
        addtag(ls(p))
        addtag(rs(p))
        tree[p].tag = 0
        
def push_up(p):
    l,r = ls(p), rs(p)
    tree[p].sum = tree[l].sum + tree[r].sum
    
    if tree[l].min < tree[r].min + tree[l].sum:
        tree[p].min = tree[l].min
        tree[p].index_min = tree[l].index_min
    else:
        tree[p].min = tree[l].sum + tree[r].min
        tree[p].index_min = tree[r].index_min
    
    if tree[l].max > tree[r].max + tree[l].sum:
        tree[p].max = tree[l].max
        tree[p].index_max = tree[l].index_max
    else:
        tree[p].max = tree[r].max + tree[l].sum
        tree[p].index_max = tree[r].index_max
        
def update(p,pl,pr,L,R):
    if L <= pl and pr <= R:
        addtag(p)
        return
    push_down(p)
    mid = (pl + pr) >> 1
    if L <= mid:
        update(ls(p),pl,mid,L,R)
    if R > mid:
        update(rs(p),mid+1,pr,L,R)
    push_up(p)
    
def query(p,pl,pr,L,R):
    if L <= pl and pr <= R:
        return tree[p]
    push_down(p)
    mid = (pl + pr) >> 1
    a,b = node(), node()
    if L <= mid:
        a = query(ls(p),pl,mid,L,R)
    else:
        a.sum = 0
        a.min = float('inf')

    if R>mid:
        b=query(rs(p),mid+1,pr,L,R)
    else:
        b.sum=0
        b.min=float('inf')
    
    ans = node()
    ans.sum = a.sum + b.sum
    if a.min < b.min + a.sum:
        ans.min = a.min
        ans.index_min = a.index_min
    else:
        ans.min = b.min + a.sum
        ans.index_min = b.index_min
    return ans

def search(l):
    left,right = l,n+1
    ans = 0
    while left < right:
        mid = (left + right) >> 1
        q = query(1,1,n,l,mid)
        presum,premin,index=q.sum,q.min,q.index_min
        if premin < 0:
            right = mid
        else:
            if premin > 0:
                left = mid + 1
            else:
                ans = max(ans,index)
                left = mid + 1
    return ans

build(1,1,n)
l,r = 0,0
for _ in range(m):
    k = list(map(int,input().split()))
    if k[0] == 1:
        l,r = k[1],k[2]
        update(1,1,n,l,r)
    else:
        l = k[1]
        print(search(l))

