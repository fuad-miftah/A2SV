class Solution:
    def fill(self,i,j,color,visited,grid,initial):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != initial or (i,j) in visited:
            return grid
    
        grid[i][j] = color
        visited.add((i,j))
        top = self.fill(i-1,j,color,visited,grid,initial)
        down = self.fill(i+1,j,color,visited,grid,initial)
        right = self.fill(i,j+1,color,visited,grid,initial)
        left = self.fill(i ,j - 1, color ,visited ,grid, initial)
        return grid

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.fill(sr,sc,color,set(),image,image[sr][sc])