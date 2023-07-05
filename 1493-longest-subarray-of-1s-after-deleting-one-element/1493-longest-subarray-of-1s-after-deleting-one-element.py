class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.extend([0, 0])
        l = 0
        zero_count = 0
        last_zero = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0 and not zero_count:
                zero_count = 1
                last_zero = r
            elif nums[r] == 0 and zero_count:
                res = max(res, r-l-1)
                l = last_zero + 1
                last_zero = r
                
        return res if res < len(nums)-2 else len(nums)-3
                