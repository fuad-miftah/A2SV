class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(indx,stack):
            if indx >= len(nums):
                if len(stack) >= 2:
                    res.add(tuple(stack.copy()))
                return

            if not stack or (indx < len(nums) and stack[-1] <= nums[indx]):
                stack.append(nums[indx])
                backtrack(indx+1,stack.copy())
                j = indx + 1
                while j < len(nums) and nums[indx] == nums[j]:
                    j+=1
                    indx+=1
                stack.pop()
                backtrack(indx+1,stack.copy())
            else:
                backtrack(indx+1,stack.copy())
        backtrack(0,[])
        return res