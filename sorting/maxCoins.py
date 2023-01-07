class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        result = 0
        piles.sort()
 
        while len(piles) > 0:
            
            piles.pop()
            result = result + piles.pop()
            piles.pop(0)

        return result




piles=[2,4,1,2,7,8]
piles = [2,4,5]
piles = [9,8,7,6,5,1,2,3,4]
sol = Solution()
sol.maxCoins(piles)