class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        targetIndice = (i for i,value in enumerate(nums) if value == target)

        return targetIndice


