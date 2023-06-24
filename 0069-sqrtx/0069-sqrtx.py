class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+2):
            if i ** 2 > x:
                return i-1
        
        