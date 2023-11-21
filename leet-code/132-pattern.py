class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        small = [nums[0]]
        for i in range(1,len(nums)):
            small.append(min(small[i-1],nums[i]))
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack and nums[stack[-1]] > nums[i]:
                if small[stack[-1]] < nums[i]:
                    return True
            stack.append(i)
                
        return False