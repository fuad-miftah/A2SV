class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            s = str(nums[i])[::-1]
            nums.append(int(s))
        res = set(nums)
        return len(res)