from collections import defaultdict
from collections import Counter
from collections import deque
import heapq
 
 
def getList():
    input_ = input().strip(" ")
    return list(map(int, input_.split(" ")))
 
def getMatrix(rows):
    res = []
    for _ in range(rows):
        res.append(getList())
    return res
 
def getNum():
    return int(input())
 
def getCount(arr):
    return Counter(arr)
 
def getString():
    return input()
 
 
def isValidPosition(grid, node):
    return 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0])
 
 
 
def DFS(grid, root, seen):
    queue = deque([(root, None)])
    color = grid[root[0]][root[1]]
    seen.add(root) 
 
    dir_= [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
 
    while queue:
        current = queue.popleft()
        
        for r, c in dir_:
            row = current[0][0] + r
            col = current[0][1] + c
 
            if isValidPosition(grid, (row, col)) and grid[row][col] == color:
                if (row, col) not in seen:
                    queue.append(((row, col), current[0]))
                    seen.add((row, col)) 
                else:
                    if current[1] != (row,col):
                        return True
 
    
    
    return False
 
    
 
 
 
 
def solution(rows, cols):
    seen = set()
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in seen:
                if (DFS(grid, (row, col), seen)):
                    return "Yes"
    return "No"
            
 
rows, cols = getList()
grid = []
for _ in range(rows):
    grid.append(getString())
 
print(solution(rows, cols))