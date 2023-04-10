class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rowl = len(mat)
        coll = len(mat[0])
        if rowl * coll == r * c:
            row = 0
            col = 0
            res = [[0]*c for ro in range(r)]
            for i in range(rowl):
                for j in range(coll):
                    res[row][col] = mat[i][j]
                    col += 1
                    if col == c:
                        col = 0
                        row += 1
            return res
        else:
            return mat