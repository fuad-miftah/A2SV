class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = defaultdict(int)
        for i in range(len(s)-1,-1,-1):
            dp[(i,i)] = 1
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    dp[(i,j)] = 2 + dp[(i+1,j-1)]
                else:
                    dp[(i,j)] = max(dp[(i,j-1)],dp[(i+1,j)])
        return dp[(0,len(s)-1)]