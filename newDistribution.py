from collections import defaultdict
n,m = map(int, input().split())
size = [1] * (n + 1)
rep = [ i for i in range(n + 1)]
 
def find(x):
    if rep[x] == x:
        return rep[x]
 
    rep[x] = find(rep[x])
    return rep[x]
def union(x,y):
    
    repx = find(x)
    repy = find(y)
 
    if repx != repy:
        if size[repx] > size[repy]:
            size[repx] += size[repy]
            rep[repy] = rep[repx]
        else:
            size[repy] += size[repx]
            rep[repy] = rep[repx]
 
for _ in range(m):
    arr = list(map(int, input().split()))
    if len(arr) > 2:
        prev = arr[1]
        for i in range(1,len(arr)):
            union(prev,arr[i])
            prev = arr[i]
    
dic = defaultdict(int)
for key in rep:
    dic[find(key)] += 1
 
res = []
for i in range(1,len(rep)):
    res.append(dic[find(rep[i])])
print(*res)