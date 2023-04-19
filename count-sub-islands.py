class Solution:
    def inbound(self,i,j,row,col):
        #if 0 <= i < row and 0 <= j < col:
        if i >= 0 and i < row and j >= 0 and j < col:
            return True
        else:
            return False
    def dfs(self,i,j,grid,visited,path):
        if self.inbound(i,j,len(grid),len(grid[0])) and (i,j) not in  visited and grid[i][j] == 1:
            path.append((i,j))
        if not self.inbound(i,j,len(grid),len(grid[0])) or (i,j) in visited or grid[i][j] == 0:
            return path
        visited.add((i,j))
        top = self.dfs(i-1,j,grid,visited,path)
        down = self.dfs(i+1,j,grid,visited,path)
        left = self.dfs(i,j-1,grid,visited,path)
        right = self.dfs(i,j+1,grid,visited,path)
        return path
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        visited2 = set()
        island2 = []
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i,j) not in visited2 and grid2[i][j] == 1:
                    output = self.dfs(i,j,grid2,visited2,[])
                    island2.append(output)

        count = 0
        for i in range(len(island2)):
            j = 0
            while j < len(island2[i]):
                x,y = island2[i][j]
                if grid1[x][y] == 0:
                    break
                j += 1
            if j == len(island2[i]):
                count += 1
                
        return count