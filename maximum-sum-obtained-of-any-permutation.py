class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*len(nums)
        for i in range(len(requests)):
            start,end = requests[i]
            prefix[start]+=1
            if end+1 < len(prefix):
                prefix[end+1]-=1
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1] + prefix[i]
        res = 0
        nums.sort(reverse = True)
        prefix.sort(reverse = True)
        
        for i in range(len(prefix)):
            res+=(nums[i]*prefix[i])
        return res % (10**9 + 7)