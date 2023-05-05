class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapify(piles)
        while k:
            popped = heappop(piles)
            heappush(piles,popped // 2)
            k -= 1
        return -1 * sum(piles)