class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < len(nums):
                while nums[i] < len(nums) and nums[i] != i:
                    cur = nums[i]
                    nums[i] = nums[cur]
                    nums[cur] = cur
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)