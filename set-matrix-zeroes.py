class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroInd = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroInd.append([i,j])
    
        for i in range(len(zeroInd)):
            row = zeroInd[i][0]
            col = zeroInd[i][1]
            for j in range(len(matrix)):
                matrix[j][col] = 0
            for k in range(len(matrix[0])):
                matrix[row][k] = 0