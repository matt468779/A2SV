class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        count = [0] * 32
        mask = 1
        for i in range(32):
            for num in nums:
                count[i] += 1 if mask & num else 0

            mask *= 2
            
        res = 0
        mul = 2**k
        for num in nums:
            others = 0
            mask = 1
            for i in range(32):
                bit = 1 if mask & num else 0
                if count[i] - bit > 0:
                    others ^= mask
                mask *= 2
                
            res = max(res, others|(num*mul))
        
        return res
                    