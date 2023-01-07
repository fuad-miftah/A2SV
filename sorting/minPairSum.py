class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pair = []
      
        nums.sort()
        while len(nums) != 0:
            pair.append(nums.pop(0) + nums.pop())
        result = max(pair)

        return result


nums = [3,5,4,2,4,6]
nums = [3,5,2,3]
sol = Solution()
sol.minPairSum(nums)