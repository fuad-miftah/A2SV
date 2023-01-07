class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = []
        while len(nums) != 0:
            result.append(nums.pop(0))
            if len(nums) != 0:
                result.append(nums.pop())
        return result


nums = [1,2,3,4,5]
nums = [6,2,0,9,7]
nums = [1,2,3,6,0]
sol = Solution()
sol.rearrangeArray(nums)