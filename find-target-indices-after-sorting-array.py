class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        targetIndice = (i for i,value in enumerate(nums) if value == target)

        return targetIndice