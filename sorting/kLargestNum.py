class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        
        nums.sort(key = lambda x : int(x), reverse = True)
        
        return nums[k-1]




nums = ["3", "6", "7", "10"]
nums = ["2","21","12", "1"]
nums = ["0","0"]
sol = Solution()
sol.kthLargestNumber(nums, 2)