class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
                return False
        return False