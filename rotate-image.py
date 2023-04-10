class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cont = True
        i = 0
        while cont:
            colLength = len(matrix) - i
            k = 0
            for r in range(i,colLength-1):
                tL = matrix[i][r]
                tR = matrix[r][colLength - 1]
                bR = matrix[colLength - 1][colLength - 1 - r + i]
                bL = matrix[colLength - 1 - r + i][i]
                
                matrix[i][r] = bL
                matrix[r][colLength - 1] = tL
                matrix[colLength - 1][colLength - 1 - r + i] = tR
                matrix[colLength - 1 - r + i][i] = bR

            i += 1
            if i > len(matrix) // 2:
                cont = False