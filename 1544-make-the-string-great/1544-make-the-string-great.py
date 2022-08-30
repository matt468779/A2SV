class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        res = ''
        while i < len(s)-1:
            if (s[i].islower() and s[i+1].isupper() and s[i] == s[i+1].lower()) or (s[i].isupper() and s[i+1].islower() and s[i].lower() == s[i+1]):
                s = s[:i] + s[i+2:]
                if i > 0:
                    i -= 1
            else:
                i += 1
                
        return s