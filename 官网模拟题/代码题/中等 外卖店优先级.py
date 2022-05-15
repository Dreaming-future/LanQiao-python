# https://www.lanqiao.cn/problems/184/learning/?is_contest=true

n,m,T = map(int,input().split())
a=[]
 
for i in range(m):
    a.append(list(map(int,input().split())))
 
#对订单的的时间进行排序，目的是算出当前订单与上一回订单之间的间隔
#从未计算出这家店没有订单的时候优先级下降数
#即：prior[idd] -= ts-order[idd]-1
a=sorted(a,key=lambda a:a[0])
 
#初始化为0
order=[0]*(n+1)#订单的时刻
prior=[0]*(n+1)#优先级的分数
flag=[0]*(n+1)#是否在优先缓存中
 
#遍历每一条订单信息
for i in range(m):
    ts = a[i][0]
    idd = a[i][1]
    #如果当前订单的时间不等于上次的订单
    #由题意每过一秒优先级减1，所以优先级减去间隔
    if ts != order[idd]:
        prior[idd] -= ts-order[idd]-1
    if prior[idd]<0: 
        prior[idd]=0#优先级最低为0
    if prior[idd]<=3: 
        flag[idd]=0
    prior[idd]+=2  #有订单则优先级加2
    if prior[idd]>5: 
        flag[idd]=1
    order[idd]=ts  #记录这次订单的时间，下此迭代使用
 
#处理到了T时刻的情况
for i in range(1,n+1):
    #如果最后一个订单不是T时刻的
    #要减去最后一趟订单时间与t的差的绝对值
    if order[i] < T:
        prior[i] -= T-order[i]
        if prior[i] <= 3: 
            flag[i]=0
 
#遍历求在缓存区的商家个数
ans=sum(flag)
print(ans) 