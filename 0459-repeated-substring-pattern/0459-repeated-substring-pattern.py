class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            if len(s) % i:
                continue
                
            res = True
            for j in range(i, len(s)):
                if s[j] != s[j%i]:
                    res = False
                    break
                    
            if res:
                return res
        
        return False