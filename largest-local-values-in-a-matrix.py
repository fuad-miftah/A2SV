class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2): 
            for j in range(n-2): 
                ans[i][j] = max(grid[row][col] for row in range(i, i+3) for col in range(j, j+3))
        return ans