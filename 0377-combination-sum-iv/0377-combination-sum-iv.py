class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        nums = set(nums)
        
        for i in range(1, target+1):
            for j in range(i+1):
                if j in nums:
                    dp[i] += dp[i-j]
        
        return dp[target]
        