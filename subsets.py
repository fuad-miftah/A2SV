class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i,num):
            if i == len(nums):  
                res.append(num)
                return
            
            backtrack(i+1,num | set([nums[i]]))
            backtrack(i+1,set(num))
            return
        backtrack(0,set([]))

        return res