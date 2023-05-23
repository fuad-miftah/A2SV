from collections import defaultdict
t = int(input())
 
for _ in range(t):
    dic = defaultdict(list)
    n,e = map(int, input().split())
    for i in range(e):
        u,v = map(int, input().split())
        dic[u].append(v)
        dic[v].append(u)
 
    y = 0
 
    for key in dic:
        if len(dic[key]) == 1:
            y += 1
    #print(dic,y)
    if y == len(dic):
        print(1,1)
    elif y == len(dic) - 1:
        print(y // 2, y // 2)
    else:
        print(len(dic) - 1 - y,y // (len(dic) - 1 - y) )