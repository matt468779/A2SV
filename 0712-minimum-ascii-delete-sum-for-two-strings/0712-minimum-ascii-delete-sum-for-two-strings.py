class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def ascii_sum(s):
            res = 0
            for char in s:
                res += ord(char)
            
            return res
        
        def solve(i, j):
            state = (i, j)
            if state in dp:
                return dp[state]
            
            if i >= len(s1) or j >= len(s2):
                res = ascii_sum(s1[i:]) + ascii_sum(s2[j:])
            
            elif s1[i] == s2[j]:
                res = solve(i+1, j+1)
            
            else:
                res = min(ord(s1[i]) + solve(i+1, j), ord(s2[j]) + solve(i, j+1))
            
            dp[state] = res
            return res
        
        dp = {}
        return solve(0, 0)
            