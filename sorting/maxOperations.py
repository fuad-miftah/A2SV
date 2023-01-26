class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        d = {}
        for x in nums:
            t = k-x
            if t in d and d[t] > 0:
                res += 1
                d[t] -= 1
            else:
                if x not in d:
                    d[x] = 0
                d[x] += 1

        return(res)

nums = [1,2,3,4]
sol = Solution()
sol.maxOperations(nums,5)