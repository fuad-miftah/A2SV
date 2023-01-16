class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l,r = 0,0
        result,total = 0,0
    
        while r < len(nums):
            total+= nums[r]
            while nums[r]* (r - l + 1) > total + k:
                total -= nums[l]
                l+=1

            result = max(result, r - l + 1)
            r+=1
        return result
