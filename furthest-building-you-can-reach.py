class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            
            if diff <= 0:
                continue
            
            if diff > 0:
                heapq.heappush(heap, diff)
            
            if len(heap) > ladders:
                brick_need = heapq.heappop(heap)
                bricks -= brick_need
            
            if bricks < 0:
                return i
        
        return n-1