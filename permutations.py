class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        mask = 0 

        def backtrack(curr):
            nonlocal mask
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if (mask >> i) & 1 == 0:
                    mask |= 1 << i
                    backtrack(curr + [nums[i]])
                    mask ^= 1 << i

        backtrack([])
        return res