class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix[0])):
            j = 1
            k = i + 1
            temp = matrix[0][i]
            while j < len(matrix) and k < len(matrix[0]):
                if matrix[j][k] != temp:
                    return False
                j += 1
                k += 1
        
        for i in range(1,len(matrix)):
            j = i + 1
            k = 1
            temp = matrix[i][0]
            while j < len(matrix) and k < len(matrix[0]):
                if matrix[j][k] != temp:
                    return False
                j += 1
                k += 1
        return True