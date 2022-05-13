import os
import sys

# 请在此输入您的代码

def lowbit(x):
    return -x&x

def update(x,d):
    while x <= n:
        tree[x] += d
        x += lowbit(x)

def getsum(x):
    ans = 0
    while x:
        ans += tree[x]
        x -= lowbit(x)
    return ans

n = int(input())
a = [0]
a.extend(list(map(int,input().split())))
b = [0]*(n+1)
# 左边逆序对
tree = [0 for _ in range(n+1)]
for i in range(1,n+1):
    update(a[i],1)
    b[i] += i - getsum(a[i])
    
tree = [0 for _ in range(n+1)]    
# 右边逆序对 
for i in range(n,0,-1):
    update(a[i],1)
    b[i] += getsum(a[i]-1)
res = 0
for i in range(1,n+1):
    res += (b[i]+1)*b[i] // 2
print(res)



#   归并排序解法
def merge(a,l,r):   
  if l>=r:  return
  mid=(l+r)//2
  tmp,i,j=[],l,mid+1
  merge(a,l,mid)
  merge(a,mid+1,r)

  while i<=mid and j<=r:
    if a[i]<=a[j]:
      tmp.append(a[i])
      i+=1
    else:
      tmp.append(a[j])
      high[a[j]]+=mid-i+1   #求出所有小朋友的high值
      j+=1
  if i<=mid:
    tmp.extend(a[i:mid+1])
  elif j<=r:
    tmp.extend(a[j:r+1])
  a[l:r+1]=tmp[:]

def binary(a,k):    #二分查找数组中与k相等的左边界下标
    l,r=0,len(a)
    while l<r:
        mid=(l+r)//2
        if a[mid]<k:
            l=mid+1
        elif a[mid]>=k:
            r=mid
    return l
        
n=int(input())
h=[-1]+list(map(int,input().split()))
pos,low,high=[0]*(n+1),[0]*(n+1),[0]*(n+1)
#pos[k]:第k高小朋友在队中的位置
#low[k]:第k高小朋友后面比它矮的小朋友数量
#high[k]:第k高小朋友前面比它高的小朋友数量

a=h[:]
a.sort()
for i in range(1,n+1):  #对h[]重新编号
    k=binary(a,h[i])
    h[i]=k      #身高从低到高重新编号
    pos[h[i]]=i #第k矮小朋友排在原队列的第i个
    a[k]-=1     #再次查到a[k]的时候查到的是后一个

merge(h,1,n)
ans=0
for i in range(1,n+1):
    k=pos[i]    #第i矮的小朋友编号
    w=i         #w表示第i矮的
    low[i]=w-1-(k-1-high[i])
    t=high[i]+low[i]
    ans+=t*(t+1)//2
print(ans)