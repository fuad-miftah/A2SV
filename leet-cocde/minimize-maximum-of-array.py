class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            res = max(res, math.ceil(prefix_sum / (i + 1)))

        return res