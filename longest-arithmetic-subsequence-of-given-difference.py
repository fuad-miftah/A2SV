class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for i in range(len(arr)):
            if arr[i] - difference in dp:
                dp[arr[i]] = dp[arr[i] - difference] + 1
            else:
                dp[arr[i]] = 1
        res = 0
        for key in dp:
            if dp[key] > res:
                res = dp[key]
        return res