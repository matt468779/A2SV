class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = 257
        ordTarget = ord(target)
        for l in letters:
            l = ord(l)
            if l > ordTarget and l < res:
                res = l
            elif l+26 < res:
                res = l+26
        
        return chr(res) if res < 123 else chr(res-26)
