class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        right = len(nums)-4
        res = float('inf')
        for left in range(4):
            res = min(res, nums[right+left]-nums[left])
        
        return res
            