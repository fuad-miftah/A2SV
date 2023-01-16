class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort()
        # output = 0
        
        # i = -1
        # while i < len(nums) - 1 and k > nums[i] + nums[i+1]:
        #     i += 1
        #     for j in range(1,len(nums)):
        #         if nums[i] + nums[j] == k:
        #             output += 1
        #             nums.remove(nums[i])
        #             nums.remove(nums[j])
                    
                
        # print(output)
        # return output
        res = 0
        d = {}
        for x in nums:
            t = k-x
            if t in d and d[t] > 0:
                print(11)
                res += 1
                d[t] -= 1
            else:
                print(22)
                if x not in d:
                    print(33)
                    d[x] = 0
                d[x] += 1
                print(d)
        print(res)
        return(res)

nums = [1,2,3,4]
sol = Solution()
sol.maxOperations(nums,5)