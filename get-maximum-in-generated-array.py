class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0,1]
        if n == 0:
            return 0
        i = 2
        while len(dp) < n + 1:
            dp.append(dp[i-1])
            if len(dp) < n + 1:
                dp.append(dp[i-1]  + dp[i])
            i += 1

        return max(dp)