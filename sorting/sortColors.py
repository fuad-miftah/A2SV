class Solution(object):
    def sortColors(self,nums):
        for i in nums:
            for j in range(len(nums)-1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]




nums = [2,0,2,1,1,0]
sol = Solution()
sol.sortColors(nums)