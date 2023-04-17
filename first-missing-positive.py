class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = 0
        while l < len(nums):
            while nums[l] <= len(nums) and nums[l] > 0 and nums[l] != l + 1 and nums[nums[l]-1] != nums[l]:
                temp = nums[nums[l] - 1]
                nums[nums[l] - 1] = nums[l]
                nums[l] = temp
            l += 1
        res = 0
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res = i + 1
                break
        if res == 0:
            return len(nums) + 1
        else:
            return res