class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            last_x = x & 1
            last_y = y & 1
            res += last_x ^ last_y
            
            x >>= 1
            y >>= 1
        
        return res