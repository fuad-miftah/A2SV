class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals:
            endAtResult = result[-1][1]

            if start <= endAtResult:
                result[-1][1] =  max(endAtResult, end)
            else:
                result.append([start,end])
        print(result)

        return result
intervals = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()
sol.merge(intervals)
