from collections import defaultdict
def dfs(node,adl,color):
    if color[node] == -1:
        color[node] = 1
    for neighbour in adl[node]:
        if color[neighbour] == -1:
            color[neighbour] = 1 - color[node]
            if not dfs(neighbour,adl,color):
                return False
        elif color[neighbour] == color[node]:
                return False
    return True

n = int(input())
while n:
    
    el = int(input())
    color = [-1] * (n + 1)
    adl = defaultdict(list)
    for i in range(el):
        a,b = list(map(int, input().split()))
        adl[a].append(b)
        adl[b].append(a)      

    bipart = True
    for i in range(n+1):
        if color[i] == -1:
            if not dfs(i,adl,color):
                bipart = False
                break
    if bipart:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")

    n = int(input())