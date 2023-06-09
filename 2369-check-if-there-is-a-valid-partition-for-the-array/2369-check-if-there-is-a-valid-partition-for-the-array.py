class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums) + 1)
        dp[0] = True
        dp[2] = nums[0] == nums[1]
        
        for i in range(2, len(nums)):
            dp[i+1] = dp[i+1] or ((nums[i] == nums[i-1]) and dp[i-1])
            dp[i+1] = dp[i+1] or ((nums[i] == nums[i-1] == nums[i-2]) and dp[i-2])
            dp[i+1] = dp[i+1] or ((nums[i] == nums[i-1]+1 == nums[i-2]+2) and dp[i-2])
        
        return dp[len(nums)]