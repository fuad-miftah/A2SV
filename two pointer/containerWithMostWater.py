class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l , r = 0 , len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res , area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res


num = [1,8,6,2,5,4,8,3,7] 
sol = Solution()
print(sol.maxArea(num))