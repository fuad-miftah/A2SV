class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def Winner(nums,start,end,turn):
            if start == end:
                return nums[start] * turn
            a = turn * nums[start] + Winner(nums,start+1,end,-turn)
            b = turn * nums[end] + Winner(nums,start,end-1,-turn)
            return turn * max(turn * a, turn * b)
        return Winner(nums,0,len(nums)-1,1) >= 0