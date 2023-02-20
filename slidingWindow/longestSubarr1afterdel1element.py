class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        res = 0
        curZero = 0
    
        for right in range(len(nums)):
            if nums[right] == 0:
                curZero += 1
            while curZero > 1:
                if nums[left] == 0:
                    curZero-=1
                left+=1
            res = max(res, right-left)
        return res