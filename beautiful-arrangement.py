class Solution:
    def countArrangement(self, n: int) -> int:
        nums = []
        for i in range(n):
            nums.append(i+1)
        res = []
        def backtrack(indx,curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in curr and (nums[i] % (indx + 1) == 0 or (indx + 1) % nums[i] == 0):
                    curr.append(nums[i])
                    backtrack(indx+1,curr.copy())
                    curr.pop()
            return
        backtrack(0,[])

        return len(res)