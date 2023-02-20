class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = sum(chalk)
        k = k % prefix
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i] 