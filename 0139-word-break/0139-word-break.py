class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}
        def solve(s):
            if not s:
                return True
            if s in dp:
                return dp[s]
            
            word = []
            for i in range(len(s)):
                word.append(s[i])
                if ''.join(word) in wordSet and solve(s[i+1:]):
                    dp[s] = True
                    return True
                
            dp[s] = False
            return False
        
        return solve(s)