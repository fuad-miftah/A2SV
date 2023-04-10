class Solution:
    def check(self,i,j,grid):
        curNums = []
        row1 = row2 = row3 = col1 = col2 = col3 = 0

        for r in range(i,i+3):
            for c in range(j,j+3):
                if grid[r][c] in curNums or grid[r][c] > 9 or grid[r][c] == 0:
                    return False
                if r == i:
                    row1 += grid[r][c]
                elif r == i + 1:
                    row2 += grid[r][c]
                else:
                    row3 += grid[r][c]

                if c == j:
                    col1 += grid[r][c]
                elif c == j + 1:
                    col2 += grid[r][c]
                else:
                    col3 += grid[r][c]

                curNums.append(grid[r][c])

        diagonal1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
        diagonal2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]

        return row1 == row2 == row3 == col1 == col2 == col3 == diagonal1 == diagonal2

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        else:
            count = 0
            for r in range(len(grid)-2):
                for c in range(len(grid[0])-2):
                    if self.check(r,c,grid):
                        count+=1

            return count