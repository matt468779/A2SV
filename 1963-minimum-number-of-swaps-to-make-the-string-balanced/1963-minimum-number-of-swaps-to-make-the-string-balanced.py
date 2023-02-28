class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, len(s)-1
        no_open, no_close = 0, 0
        res = 0
        while l < r:
            if s[l] == ']' and no_open > 0:
                no_open -= 1
                l += 1
                continue
            
            if s[r] == '[' and no_close > 0:
                no_close -= 1
                r -= 1
                continue
                
            if s[l] == ']' and s[r] == '[':
                no_open += 1
                no_close += 1
                res += 1
                l += 1
                r -= 1
                
            if s[l] == '[':
                no_open += 1
                l += 1
                
            if s[r] == ']':
                no_close += 1
                r -= 1
                
        return res