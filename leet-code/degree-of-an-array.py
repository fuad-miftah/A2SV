class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        first_and_last = {}
        deg = 0
        
        for i in range(len(nums)):
            freq[nums[i]] += 1
            deg = max(deg, freq[nums[i]])
            if nums[i] in first_and_last:
                first_and_last[nums[i]][1] = i
            else:
                first_and_last[nums[i]] = [i,i]
                
        res = len(nums)
                
        for num in freq:
            if freq[num] != deg:
                continue
            res = min(res, first_and_last[num][1] - first_and_last[num][0] + 1)

        return res
        