class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= dp:
                dp = i
                
        return 0 == dp
                        