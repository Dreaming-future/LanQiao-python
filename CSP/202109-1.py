# http://118.190.20.162/view.page?gpid=T129

n = int(input())
a = list(map(int,input().split()))
        
import itertools
res1, res2 = sum(a), 0
res3 = 0    
for k,b in itertools.groupby(a):
    res2 += k
print(res1,res2,sep='\n')