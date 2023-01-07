class Solution(object):
    def targetIndices(self, nums, target):
        targetIndice = []
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        i = 0

        while i < len(nums):
            if nums[i] == target:
                targetIndice.append(i)
            i = i + 1


        return targetIndice