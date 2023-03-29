class Solution:
    
    def reverse (self, nums, i, j) :
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        l = 0 
        r = len(nums)-1
        self.reverse(nums,l,r)
        self.reverse(nums,l,k-1)
        self.reverse(nums,k,r)