class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0.0
        l = 0
        total = sum(nums[l:k])
        av = total / k
        res = av
        for r in range(k,len(nums)):
            total+=nums[r]
            total-=nums[l]
            av = total / k
            res = max(res, av)
            l+=1
            
        return res