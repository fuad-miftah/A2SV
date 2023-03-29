class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        sortedArr = sorted(nums)
        for i in nums:
            count.append(sortedArr.index(i))

        return count