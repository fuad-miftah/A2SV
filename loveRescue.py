from collections import defaultdict
t = int(input())
n1 = input()
n2 = input()
 
size = defaultdict(lambda : 1)
rep = {}
for i in range(97,123):
    rep[chr(i)] = chr(i)
 
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
res = []
for i in range(t):
    s1 = find(n1[i])
    s2 = find(n2[i])
    if s1 != s2:
        res.append((s1,s2))
        union(s1,s2)
print(len(res))
for i in range(len(res)):
    print(res[i][0],res[i][1])