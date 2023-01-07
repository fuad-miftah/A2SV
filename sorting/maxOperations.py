class Solution(object):
    def maxOperations(self, nums, k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        output = 0
        
        i = -1
        while i < len(nums) - 1 and k > nums[i] + nums[i+1]:
            i += 1
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == k:
                    output += 1
                    nums.remove(nums[i])
                    nums.remove(nums[j])
                    
                
        print(output)
        return output