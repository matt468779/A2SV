class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        found_word = False
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                found_word = True
                res += 1
            elif found_word:
                break
        
        return res