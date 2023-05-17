class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def findComplement(num: int) -> int:
            res = 0
            i = 0
            while num:
                if not num & 1:
                    res += 2 ** i
                i += 1
                num >>= 1

            return res
        
        res = 0
        mask = 1
        for i in range(32):
            count = 0
            for num in nums:
                if mask & num:
                    count += 1
                    
            res += (count%3) * 2**i
            mask *= 2
            
        if res == 2**31:
            return -res
        if (2**31) & res:
            return -findComplement(res-1)
        return res