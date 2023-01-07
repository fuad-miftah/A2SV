import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        result = sorted(nums, key=lambda x: (counts[x], x), reverse=True)
        output = []
        i = 0
        while len(output) < k:
            if result[i] not in output:
                output.append(result[i])
            i+=1
    
        return output
nums = [1,1,1,2,2,3]
sol = Solution()
print(sol.topKFrequent(nums,2))