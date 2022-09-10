class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k > n/2:
            res = 0
            for i in range(1,n):
                diff = prices[i] - prices[i-1]
                if diff > 0:
                    res += diff
            return res
                    
        dp = [0] * n
        
        for _ in range(k):
            pos = -prices[0]
            profit = 0
            for i in range(1, n):
                pos = max(pos, dp[i]-prices[i])
                profit = max(profit, prices[i]+pos)
                dp[i] = profit

        return dp[-1]