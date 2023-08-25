class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def solve(i1, i2, i3):
            state = (i1, i2, i3)
            if state in dp:
                return dp[state]
            if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
                return True
            
            res1, res2 = False, False
            if i1 < len(s1) and i3 < len(s3) and s3[i3] == s1[i1]:
                res1 = solve(i1+1, i2, i3+1)
            if i2 < len(s2) and i3 < len(s3) and s3[i3] == s2[i2]:
                res2 = solve(i1, i2+1, i3+1)
            
            dp[state] = res1 or res2
            return dp[state]
        
        return solve(0, 0, 0)