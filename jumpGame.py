class Solution:
    def maxResult(self, nums , k):
        queue = []
        
        i = 0
        while i < len(nums):
            largeInd = i

            n = 0
            while i < len(nums) and n < k :
                
                if nums[largeInd] < nums[i]:
                    largeInd = i
                i += 1
                n += 1
            queue.append(nums[largeInd])
            i = largeInd + 1

        res = 0
        for i in queue:
            res += i
        print(res)
        return res

nums = [1,-1,-2,4,-7,3]
nums = [10,-5,-2,4,0,3]
nums = [1,-5,-20,4,-1,3,-6,-3]
sol = Solution()
sol.maxResult(nums,2)