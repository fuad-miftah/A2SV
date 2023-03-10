class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(n,res):
            if n == 0:
                return [1]
            if n == 1:
                return [1,1]

            r = helper(n-1,res[:])
            for i in range(1,len(r)):
                res.append(r[i]+r[i-1])
            res.append(1)

            return res
        #print(helper(rowIndex,[1]))
        return helper(rowIndex,[1])