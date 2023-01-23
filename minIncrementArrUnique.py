class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        minAvailable = 0

        nums.sort()

        for num in nums:
            ans += max(minAvailable - num, 0)
            minAvailable = max(minAvailable, num) + 1

        return ans