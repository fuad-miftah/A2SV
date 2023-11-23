class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            cur = [1]
            for j in range(1,len(res[-1])):
                cur.append(res[-1][j] + res[-1][j-1])
            cur.append(1)
            res.append(cur[:])
        return res


        