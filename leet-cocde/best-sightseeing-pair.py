class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        maxval = 0            
        for i in range(1, len(values)):
            maxval = max(maxval, values[i-1]+i-1)
            res = max(res, maxval+values[i]-i)

        return res