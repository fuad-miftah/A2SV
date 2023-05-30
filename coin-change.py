class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def helper(amount):
            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            cur = inf
            for coin in coins:
                if amount - coin >= 0:
                    ans = helper(amount-coin)
                    cur = min(cur, ans + 1)
            dp[amount] = cur
            return cur
  
        res = helper(amount)
        if res == inf:
            return -1
        else:
            return res