class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for _ in range(32):
            ones = 0
            zeroes = 0
            for i in range(len(nums)):
                last_bit = nums[i] & 1
                
                ones += last_bit
                zeroes += not last_bit
                
                nums[i] >>= 1
                
            res += ones * zeroes
        
        return res