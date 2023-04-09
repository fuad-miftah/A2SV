class Solution:
    def count(self,i,j,visited,grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
            return 0
        
        visited.add((i,j))
        
        top = self.count(i-1,j,visited,grid)
        down = self.count(i+1,j,visited,grid)
        right = self.count(i,j+1,visited,grid)
        left = self.count(i,j-1,visited,grid)
    
        return 1 + top + down + right + left
            
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    area = self.count(i,j,visited,grid)
                    maxArea = max(maxArea, area)
        return maxArea