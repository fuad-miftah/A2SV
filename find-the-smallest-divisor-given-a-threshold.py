class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        l = 1
        r = max(nums)
        while l <= r:
            mid = (r + l) // 2
            total = 0
            for num in nums:
                total+=ceil(num/mid)
            if total > threshold:
                l = mid + 1
            else:
                r = mid - 1
        return r + 1