class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = len(prices)
        prices.append(-1)
        j = 0
        for i in range(len(prices)-1):
            if prices[i] - prices[i+1] == 1:
                j += 1
            else:
                count += (j*(j+1))//2
                j = 0
                
        return count