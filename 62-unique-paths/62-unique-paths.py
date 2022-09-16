class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l, s = max(m, n), min(m, n)
        dp = [1] * s
        for i in range(l-1):
            for j in range(s-2, -1, -1):
                dp[j] += dp[j+1]
                
        return dp[0]