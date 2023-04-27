class Solution:
    def inbound(sself,i,j,row,col):
        if 0 <= i < row and 0 <= j < col:
            return True
        return False
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        visited = set([(0,0)])
        directions = [(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
        queue = deque([(0,0)])
        count = 0
        while queue and (len(grid)-1, len(grid[0]) - 1) not in visited:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                for r,c in directions:
                    if self.inbound(r + node[0] ,c + node[1],len(grid),len(grid[0])) and (r + node[0],c + node[1]) not in visited and grid[r + node[0]][c + node[1]] == 0:
                        queue.append((r + node[0],c + node[1]))
                        visited.add((r + node[0],c + node[1]))
            count += 1
        if (len(grid)-1, len(grid[0]) - 1) in visited:
            return count + 1
        else:
            return -1