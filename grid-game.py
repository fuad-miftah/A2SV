class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        col = len(grid[0]) + 1
        prefix = [[0]*col for i in range(2)]
        for i in range(2):
            for j in range(col-1):
                prefix[i][j+1] = prefix[i][j] + grid[i][j]

        r = 0
        c = 1
        while r != 1 and c < col:
            x = r
            y = c
            if prefix[r][col-1] - prefix[r][c] < prefix[1][c]:
                r+=1
            else:
                c+=1
            grid[x][y-1] = 0
            
        while c < col:
            grid[r][c-1] = 0
            c+=1
        
        s1 = 0
        for i in range(len(grid[0])):
            s1+=grid[0][i]
        s1+=grid[1][len(grid[0])-1]
        s2 = 0
        for i in range(len(grid[0])):
            s2+=grid[1][i]
        
        
        return s1 if s1 > s2 else s2