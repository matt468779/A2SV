class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit_count_num2 = 0
        while num2:
            bit_count_num2 += num2 & 1
            num2 >>= 1
        
        mask = 1
        temp_num1 = num1
        while temp_num1:
            temp_num1 >>= 1
            mask <<= 1
        
        res = 0
        while mask and bit_count_num2:
            if mask & num1:
                bit_count_num2 -= 1
                res ^= mask
            mask >>= 1
        
        mask = 1
        while bit_count_num2:
            if not (mask & res):
                bit_count_num2 -= 1
                res ^= mask
            mask <<= 1
        
        return res
                