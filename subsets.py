class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i,num):
            if i == len(nums):  
                res.append(num.copy())
                return
            num.append(nums[i])
            backtrack(i+1,num)
            num.pop()
            backtrack(i+1,num)
        backtrack(0,[])
        return res