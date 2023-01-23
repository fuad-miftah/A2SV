class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        res = 0
        i = len(citations) - 1
        while i > 0:
            if len(citations) - i >= citations[i]:
                res = citations[i]
                break
            i -= 1
        print(res)
        return res






citations = [3,0,6,1,5]
citations = [1,3,1]
sol = Solution()
sol.hIndex(citations)
