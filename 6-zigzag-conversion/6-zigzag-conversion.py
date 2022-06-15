class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        
        res = ""
        gap = 2*(numRows - 1)
        for i in range(0, len(s), gap):
            res += s[i]
          
        for i in range(1, numRows-1):
            res += s[i]
            entered = False
            j = i
            for j in range(i, len(s)-gap, gap):
                res += s[j+gap-i*2]
                res += s[j+gap]
                entered = True
                
            if not entered and j+gap-i*2 < len(s):
                res += s[j+gap-i*2]
            elif j+2*gap-i*2 < len(s):
                res += s[j+2*gap-i*2]
            
        for i in range(numRows-1, len(s), gap):
            res += s[i]
        
        return res