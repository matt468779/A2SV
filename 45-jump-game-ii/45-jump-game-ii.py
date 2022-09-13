class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            j = i+1
            if nums[i] > nums[i+1] and dp[i+1] != float('inf'):
                j += nums[i+1]-2
                dp[i] = max(0, dp[i+1]-1)

            while j < len(nums) and j <= i+nums[i]:
                dp[i] = min(dp[i], dp[j])
                j += 1
            dp[i] += 1
        
        print(dp)
        return dp[0]