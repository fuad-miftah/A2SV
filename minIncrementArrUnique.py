class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        minNextAvailableNum = 0

        nums.sort()

        for num in nums:
            ans += max(minNextAvailableNum - num, 0)
            minNextAvailableNum = max(minNextAvailableNum, num) + 1

        return ans