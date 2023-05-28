class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        small = middle = inf

        for i in range(len(nums)):
            if middle < nums[i]:
                return True
            if small >= nums[i]:
                small = nums[i]
            else:
                middle = nums[i]

        return False