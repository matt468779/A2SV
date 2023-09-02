class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [float(inf)] * (len(s)+1)
        dp[0] = 0
        words_set = set(dictionary)
        for i in range(len(s)):
            for j in range(i+1):
                temp_word = s[j:i+1]
                temp = dp[j]
                if temp_word not in dictionary:
                    temp += i-j+1
                    
                dp[i+1] = min(dp[i+1], temp)
        
        return dp[-1]