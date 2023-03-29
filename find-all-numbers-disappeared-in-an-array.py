class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            while nums[i] != -1 and nums[nums[i]-1] != -1:
                cur = nums[i]
                nums[i] = nums[cur-1]
                nums[cur-1] = -1
        for i in range(len(nums)):
            if nums[i] != -1:
                res.append(i+1)
        return res