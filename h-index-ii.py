class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        l = 0
        r = N - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] == N - mid:
                return N - mid
            elif citations[mid] < N - mid:
                l = mid + 1
            else:
                r = mid - 1
        return N - l