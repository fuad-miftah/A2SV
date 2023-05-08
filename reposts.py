
from collections import defaultdict
import string
t = int(input())
adl = defaultdict(list)
names = set()
 
count = 0
def dfs(name,visited):
    global count
    visited.add(name)
    count += 1
    for child in adl[name]:
        if child not in visited:
            dfs(child,visited)
for _ in range(t):
    a , b, c = (input().split())
    a = a.lower()
    c = c.lower()
    if a not in names:
        names.add(a)
    if c not in names:
        names.add(c)
    adl[a].append(c)
    res = 0
 
 
    for name in names:
        count = 0
        dfs(name,set())
        res = max(res,count)
    
print(res)