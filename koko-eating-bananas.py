class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            count = 0
            
            for j in range(len(piles)):
                count+= ceil(piles[j] / mid)

            if count > h:
                l = mid + 1
            else:
                r = mid - 1
        return r+1