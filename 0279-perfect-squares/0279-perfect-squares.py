class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1
        squares = [i**2 for i in range(1, isqrt(n) + 1)]
        for i in range(2, n+1):
            j = 0
            while j < len(squares) and squares[j] <= i:
                dp[i] = min(dp[i], dp[i-squares[j]])
                j += 1
            
            dp[i] += 1
        
        return dp[n]