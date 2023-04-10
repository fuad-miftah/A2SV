class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l , r, t, b = 0, len(matrix[0]), 0, len(matrix)
        res = []
        while l < r and b > t:
            for i in range(l,r):
                res.append(matrix[l][i])
            t+=1
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1
            if r == l or b == t:
                break
            for i in range(r - 1,l-1,-1):
                res.append(matrix[b-1][i])
            b-=1
            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1

        return res