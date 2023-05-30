class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(0,0):1}
        def helper(curr):
            nonlocal m , n
            if curr in dp:
                return dp[curr]
            ans = 0
            for r,c in [(-1,0),(0,-1)]:
                nr = r + curr[0]
                nc = c + curr[1]
                inbound = 0 <= nr < m and 0 <= nc < n
                if inbound:
                    ans += helper((nr,nc))
            dp[curr] = ans
            return ans
        return helper((m-1,n-1))