class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = []
        sortedArr = sorted(nums)
        for i in nums:
            count.append(sortedArr.index(i))
                                
        return count



nums = [8, 1, 2, 2, 3]
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))