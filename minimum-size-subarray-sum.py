class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        maxi=float("inf")
        sums=0
        
        while j < len(nums):                
            sums+=nums[j]
            while sums>=target:         
                maxi=min(maxi,j-i+1)    
                sums-=nums[i]
                i+=1
            j+=1

        return maxi if maxi!=float("inf") else 0