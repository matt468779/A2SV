class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            lastA = a & 1
            lastB = b & 1
            lastC = c & 1
            
            if lastC == 0:
                res += lastA + lastB
            else:
                res += not (lastA | lastB)
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return res