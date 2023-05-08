t = int(input())
 
 
for _ in range(t):
    mat = []
    reached = False
    n = int(input())
    n1 = list(map(int , input()))
    n2 = list(map(int , input()))
    # mat.append(n1)
    # mat.append(n2)
 
    #res = dfs(0,0,set(),mat)
    canReach = True
    for i in range(len(n1)):
        if n1[i] == 1 and n2[i] == 1:
            canReach = False
            break
    if canReach:
        print("YES")
    else:
        print("NO")