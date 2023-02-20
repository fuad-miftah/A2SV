class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            leftSum+=nums[i]
            if total - leftSum == leftSum - nums[i]:
                return i
        return -1