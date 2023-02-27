class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        word = Counter(s[:3])
        res = 1 if len(word) == 3 else 0
        for i in range(3, len(s)):
            if word[s[i-3]] == 1:
                word.pop(s[i-3])
            else:
                word[s[i-3]] -= 1
            
            if s[i] not in word:
                word[s[i]] = 1
            else:
                word[s[i]] += 1
        
            if len(word) == 3:
                res += 1
        
        return res