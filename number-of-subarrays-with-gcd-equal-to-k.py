class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            gcdd = nums[i]
            if gcdd == k:
                res += 1
            for j in range(i+1,len(nums)):
                gcdd = gcd(gcdd,nums[j])
                if gcdd == k:
                    res += 1

        return res