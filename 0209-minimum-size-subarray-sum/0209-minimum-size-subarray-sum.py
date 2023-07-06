class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        sub_sum = 0
        res = float('inf')
        while r < len(nums) or sub_sum >= target:
            if sub_sum >= target:
                res = min(res, r-l)
                sub_sum -= nums[l]
                l += 1
            else:
                sub_sum += nums[r]
                r += 1
        
        return res if res != float('inf') else 0