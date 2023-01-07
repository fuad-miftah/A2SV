class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        highstFreq = 1
        inte = k
        nums.sort()
        print(nums)

        i = 0
        while inte > 0 and highstFreq < len(nums) - i
            
            freq = 1
            z = 1
            for j in range(i+1,len(nums)):
                i += 1
                
                if inte > 0:
                    
                    if (nums[j] - nums[j-1]) * z <= inte:
                        freq += 1
                        inte = inte - ((nums[j] - nums[j-1]) * z)
                        print(inte)
                        z +=1
                        
                        if freq > highstFreq:
                            highstFreq = freq
                    else:
                        inte = -1
                        break
                else:
                    break
                    inte = -1
                   
                    
        return highstFreq