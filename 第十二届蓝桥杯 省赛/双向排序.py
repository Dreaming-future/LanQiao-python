import os
import sys

def ls(p): return p << 1 # 2*k
def rs(p): return p << 1 | 1 # 2*k+1

def push_up(p):
    tree[p] = tree[ls(p)] + tree[rs(p)]
    
def build(p,pl,pr):
    if pl == pr:
        tree[p] = 1 # 开始全部标记为1，表示在生序区
        return
    mid=(pl+pr)>>1
    build(ls(p),pl,mid)
    build(rs(p),mid+1,pr)
    push_up(p)
    
# 增加lazy_tag标记
def addtag(p,pl,pr,d):
    tag[p] = d
    tree[p] = d*(pr-pl+1) 

def push_down(p,pl,pr):
    if ~tag[p] != 0:
        mid = (pl + pr) >> 1
        addtag(ls(p),pl,mid,tag[p])
        addtag(rs(p),mid+1,pr,tag[p])
        tag[p] = -1
        
# 把 1 变成 0
def update0(p,pl,pr,cnt):
    if cnt == 0: return
    if tree[p] == cnt:
        addtag(p,pl,pr,0)
        return 
    mid = (pl + pr)>>1
    push_down(p,pl,pr)
    if tree[ls(p)]>cnt:
        update0(ls(p),pl,mid,cnt)
    else:
        cnt -= tree[ls(p)]
        addtag(ls(p),pl,mid,0)
        update0(rs(p),mid+1,pr,cnt)    
    push_up(p)

# 把0变成1
def update1(p,pl,pr,cnt):
    if cnt==0:return
    if pr-pl+1-tree[p]==cnt:
        addtag(p,pl,pr,1)
        return
    mid=(pl+pr)>>1
    push_down(p,pl,pr)
    if mid-pl+1-tree[ls(p)]>cnt:
        update1(ls(p),pl,mid,cnt)
    else:
        cnt-=(mid-pl+1-tree[ls(p)])
        addtag(ls(p),pl,mid,1)
        update1(rs(p),mid+1,pr,cnt)
    push_up(p)

def query(p,pl,pr,L,R):
    if L<=pl and pr<=R:
        return tree[p]
    push_down(p,pl,pr)
    mid=(pl+pr)>>1
    res=0
    if L<=mid:
        res+=query(ls(p),pl,mid,L,R)
    if R>mid:
        res+=query(rs(p),mid+1,pr,L,R)
    return res

n,m = map(int,input().split())
tree = [0 for _ in range(n<<2)]
tag = [-1 for _ in range(n<<2)]

for _ in range(m):
    op,num = map(int,input().split())
    if op == 0:
        pos = n - tree[1]
        cnt = max(0, num-pos)
        update0(1,1,n,cnt)
    elif op==1:
        pos=tree[1]
        cnt=max(0,n-num+1-pos)
        update1(1,1,n,cnt)
ans1,ans2=[],[]
for i in range(1,n+1):
    if query(1,1,n,i,i)==0:
        ans1.append(i)
    else:
        ans2.append(i)
for x in ans1[::-1]+ans2:
    print(x,end=' ')