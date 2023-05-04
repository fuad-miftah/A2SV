class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapify(stones)
        while len(stones) > 1:
            largest = heappop(stones)
            secondL = heappop(stones)
            if largest != secondL:
                heappush(stones,largest-secondL)
        
        return -1 * stones[0] if stones else 0