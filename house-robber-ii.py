class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        dp1 = [nums[0],nums[1]]
        for i in range(2,len(nums)-1):
            dp1.append(max(dp1[i-2] + nums[i], dp1[i-1] - nums[i-1] + nums[i]))

        dp2 = [0,nums[1],nums[2]]
        for i in range(3,len(nums)):
            dp2.append(max(dp2[i-2] + nums[i], dp2[i-1] - nums[i-1] + nums[i]))
        
        return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])