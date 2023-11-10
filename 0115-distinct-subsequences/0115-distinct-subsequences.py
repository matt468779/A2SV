class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        
        dp = [[-1]*len(t) for _ in range(len(s))]
        def solve(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0
            if i < len(s) and j < len(t):
                if s[i] == t[j]:
                    res += solve(i+1, j+1)
                res += solve(i+1, j)
            
            dp[i][j] = res
            return res
        
        return solve(0, 0)