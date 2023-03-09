class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*(len(nums))
        for i in range(len(nums)):
            if stack:
                while stack and stack[-1][1] < nums[i]:
                    index,val = stack.pop()
                    res[index] = nums[i]
                stack.append([i,nums[i]])
            else:
                stack.append([i,nums[i]])
        for i in range(len(nums)):
            if stack:
                while stack and stack[-1][1] < nums[i]:
                    index,val = stack.pop()
                    res[index] = nums[i]
                stack.append([i,nums[i]])
            else:
                stack.append([i,nums[i]])
       
        return res