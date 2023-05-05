class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        newm = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                newm.append(matrix[i][j])
        heapify(newm)
        i = 0
        while i < k-1:
            heappop(newm)
            i += 1
        return heappop(newm)