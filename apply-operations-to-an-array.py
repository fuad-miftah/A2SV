class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        
        for i in range(len(nums)):
            j = i
            while j < len(nums)-1 and nums[j] == 0:
                j+=1
            nums[j],nums[i] = nums[i],nums[j]
        return nums