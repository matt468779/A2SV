class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bit_count = [0] * 32
        
        def check_if_set(num):
            i = 0
            while num:
                if (num & 1) and bit_count[i] == 1:
                    return True
                num >>= 1
                i += 1
                
            return False
        def remove_bits(num):
            i = 0
            while num:
                if (num & 1) and bit_count[i] == 1:
                    bit_count[i] = 0
                num >>= 1
                i += 1
        
        def set_bits(num):
            i = 0
            while num:
                if num & 1:
                    bit_count[i] = 1
                num >>= 1
                i += 1
                
        l = 0
        r = 0
        res = 1
        while r < len(nums):
            if not check_if_set(nums[r]):
                set_bits(nums[r])
                r += 1
            else:
                remove_bits(nums[l])
                l += 1
            
            res = max(res, r-l)
        
        return res
