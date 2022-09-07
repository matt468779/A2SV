class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0] * (len(prices)+2)
        
        for i in range(len(prices)-2, -1, -1):
            for j in range(i+1, len(prices)):
                p = max(0, prices[j]-prices[i])
                profit[i] = max(profit[i], p + profit[j+2])
            profit[i] = max(profit[i], profit[i+1])

        return profit[0]