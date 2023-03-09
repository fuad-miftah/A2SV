class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        hashMap = {0:1}
        curSum = 0
        res = 0
        for i in nums:
            curSum+=i
            dif = curSum - k
            res += hashMap.get(dif,0)
            hashMap[curSum] = 1 + hashMap.get(curSum, 0)
        return res