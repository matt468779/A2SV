class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        half = total // 2
        dp = {}
        def solve(i, summ):
            state = (i, summ)
            
            if state in dp:
                return dp[state]
            
            if summ == half:
                return True
            if summ > half or i >= len(nums):
                return False
            
            res = solve(i+1, summ) or solve(i+1, summ+nums[i])
            dp[state] = res
            return res
        
        return solve(0, 0)