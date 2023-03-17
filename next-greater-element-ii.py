class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*(len(nums))
        for j in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    index = stack.pop()
                    res[index] = nums[i]
                stack.append(i)
       
        return res