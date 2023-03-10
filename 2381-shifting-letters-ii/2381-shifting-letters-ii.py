class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre_shift = [0] * len(s)
        
        for shift in shifts:
            pre_shift[shift[0]] += 1 if shift[2] else -1
            if shift[1] < len(s)-1:
                pre_shift[shift[1]+1] += -1 if shift[2] else 1
                
        for i in range(1, len(pre_shift)):
            pre_shift[i] += pre_shift[i-1]
            
        res = []
        for i in range(len(s)):
            pre_shift[i] += ord(s[i]) - ord('a')
            pre_shift[i] = chr((pre_shift[i]%26) + ord('a'))
            
        return ''.join(pre_shift)