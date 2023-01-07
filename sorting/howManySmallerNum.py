class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = []
        for i in range(len(nums)):
            cou = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    cou = cou + 1
            count.append(cou)
                                
        return count



nums = [8, 1, 2, 2, 3]
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))