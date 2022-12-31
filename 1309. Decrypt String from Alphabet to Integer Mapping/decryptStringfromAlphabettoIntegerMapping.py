class Solution:
    def freqAlphabets(self, s: str) -> str:
        s += '00'
        res = []
        i = 0
        while i < len(s)-2:
            if s[i+2] == '#':
                res.append(chr(int(s[i:i+2])+96))
                i += 3
            else:
                res.append(chr(int(s[i])+96))
                i += 1
        
        return ''.join(res)
