class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        count = 0
        temp = nums[0]
        for i in nums:
            temp = temp & i
        if temp != 0:
            return 1
        temp = nums[0]
        for i in range(len(nums)):
            temp = temp & nums[i]
            if temp == 0:
                count += 1
                if i < len(nums) - 1:
                    temp = nums[i + 1]
        return count