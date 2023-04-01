from collections import defaultdict
testcase = int(input())
for i in range(testcase):
    m,n = list(map(int, input().split()))
    grid = []
    for i in range(m):
        grid.append(list(map(int, input().split())))
        
    dicl = defaultdict(int)
    dicr = defaultdict(int)
    
    for i in range(m):
        for j in range(n):
            dicl[i-j] += grid[i][j]
            dicr[i+j] += grid[i][j]
    res = 0
    for i in range(m):
        for j in range(n):
            s = dicl[i-j] + dicr[i+j] - grid[i][j]
            res = max(res, s)
    print(res)