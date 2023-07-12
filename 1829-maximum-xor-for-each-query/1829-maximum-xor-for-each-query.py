class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        def invert(num):
            res = 0
            mask = 1
            for _ in range(maximumBit):
                num ^= mask
                mask *= 2
            
            return num
        
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        res = []
        for i in range(len(nums)-1, -1, -1):
            res.append(invert(total_xor))
            total_xor ^= nums[i]
            
        return res