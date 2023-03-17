class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(i,num):
            if len(nums) == i:
                ans.append(num.copy())
                return
            num.append(nums[i])
            backtrack(i+1,num)
            while i < len(nums)-1:
                if nums[i] == nums[i+1]:
                    i+=1
                else:
                    break
            num.pop()
            backtrack(i+1,num)
        
        backtrack(0,[])
        return ans