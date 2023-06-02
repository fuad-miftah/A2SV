class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dfs(indx,state):
            if indx >= len(prices):
                return 0
            if (indx,state) in memo:
                return memo[(indx,state)]
            if state:
                sell = dfs(indx+1,False) + prices[indx] - fee
                not_sell = dfs(indx+1, True)
                profit = sell +  - fee
                memo[(indx, state)] = max(sell,not_sell)
            else:
                buy = dfs(indx+1,True) - prices[indx]
                not_buy = dfs(indx+1,False)
                memo[(indx,state)] = max(buy,not_buy)
            return memo[(indx,state)]
        return dfs(0,False)