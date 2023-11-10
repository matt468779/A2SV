class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1]*len(s) for _ in range(len(s))]
        def solve(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                return 2 + solve(i+1, j-1)
            
            dp[i][j] = max(solve(i+1, j), solve(i, j-1))
            return dp[i][j]
        
        return solve(0, len(s)-1)