class Solution:
    def bfs(self, q,visited,grid):
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            node = q.popleft()
            for r,c in directions:
                nr = r + node[0]
                nc = c + node[1]
                inbound = 0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                if inbound and (nr,nc) not in visited and grid[nr][nc] == 1:
                    q.append((nr,nc))
                    visited.add((nr,nc))
        return visited
    
    def bfs2(self,q,visited,grid):
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        level = 0
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                for r,c in directions:
                    nr = r + node[0]
                    nc = c + node[1]
                    inbound = 0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                    if inbound and (nr,nc) not in visited and grid[nr][nc] == 0:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                    elif inbound and (nr,nc) not in visited and grid[nr][nc] == 1:
                        return level
            level += 1

    def shortestBridge(self, grid: List[List[int]]) -> int:
        cont = True
        i = 0
        q = deque()
        visited = set()
        while cont and i < len(grid):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
                    cont = False
                    break
            i += 1
        firstIsland = self.bfs(q,visited,grid)
        visited = firstIsland
        firstIsland = deque(firstIsland)
        res = self.bfs2(firstIsland,visited,grid)
        return res