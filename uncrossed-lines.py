class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def dp(curr,start):
            if (curr,start) in memo:
                return memo[(curr,start)]
            if start >= len(nums2) or curr >= len(nums1):
                return 0
            ans = 0
            for i in range(start,len(nums2)):
                if nums1[curr] == nums2[i]:
                    ans = dp(curr + 1,i + 1) + 1
                    break
            ans = max(ans,dp(curr + 1,start))
            memo[(curr,start)] = ans
            return ans
        return dp(0,0)