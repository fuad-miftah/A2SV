class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def Winner(l,r,t):
            if l > r:
                return 0
            if t:
                return max(nums[l]+Winner(l+1,r,not t), nums[r]+Winner(l,r-1,not t))
            else:
                return min(-nums[l]+Winner(l+1,r,not t), -nums[r]+Winner(l,r-1,not t))
        res = Winner(0,len(nums)-1,True)
        return res >= 0