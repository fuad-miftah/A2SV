class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        result = 0
        piles.sort()
 
        #print(piles)
        #for i in piles:
        while len(piles) > 0:
            
            piles.pop()
            result = result + piles.pop()
            piles.pop(0)
            #print(piles)
            
        #print(result)
        return result