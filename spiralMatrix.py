class Solution(object):
    def spiralOrder(self, matrix):
        l , r, t, b = 0, len(matrix[0]), 0, len(matrix)
        res = []
        while l < r and b > t:
            for i in range(l,r):
                res.append(matrix[l][i])
            t+=1
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1
            if r == l or b == t: break
            for i in range(r - 1,l-1,-1):
                res.append(matrix[b-1][i])
            b-=1
            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        print(res)
        return res




matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
sol.spiralOrder(matrix)