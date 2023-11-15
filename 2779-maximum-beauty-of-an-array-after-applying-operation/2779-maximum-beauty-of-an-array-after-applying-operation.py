class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, res = 0, 0, 0
        while l <= r and r < len(nums):
            while nums[r]-nums[l] > 2*k:
                l += 1
                
            res = max(res, r-l+1)
            r += 1
            
        return res