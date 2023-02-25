class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(word):
            word_set = set(word)
            i = 0
            while i < len(word) and word[i].lower() in word_set and word[i].upper() in word_set:
                i += 1
            return i == len(word)
        
        res = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                word = s[i:j+1]
                if is_nice(word) and len(word) > len(res):
                    res = word
        
        return res