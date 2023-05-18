class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        mask = 1
        patch = 0
        for i in range(32):
            if left & mask:
                if left + patch+1 > right:
                    res |= mask
            else:
                patch |= mask
                
            mask *= 2
            
        return res