class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=1
        l = 0
        for r in range(len(nums)):
            if nums[r] == nums[l]:
                continue
            else:
                res+=1
                l+=1
                nums[l] = nums[r]
        return res