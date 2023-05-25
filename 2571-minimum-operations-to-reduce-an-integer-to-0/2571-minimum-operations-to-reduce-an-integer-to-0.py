class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        ones = zeroes = 0
        finished = False
        while n or not finished:
            if n & 1 == 1:
                ones += 1
            else:
                zeroes += 1
                if zeroes == 1 and ones == 1:
                    res += 1
                    zeroes = ones = 0
                elif ones > 1 and zeroes == 1:
                    res += 1
                    zeroes = 0
                    ones = 1
                else:
                    zeroes = 0
                    
            if n == 0 and not finished:
                finished = True
            n >>= 1
            
        return res+ones