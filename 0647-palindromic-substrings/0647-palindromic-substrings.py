class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[-1]*len(s) for _ in range(len(s))]
        
        def isPalindrome(i, j):
            if i == j or j < i:
                return True
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = s[i] == s[j] and isPalindrome(i+1, j-1)
            
            return dp[i][j]
        
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    res += 1
        
        return res