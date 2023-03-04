class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        dp = [0] * len(nums)
        res = 0
        for i in range(len(nums)):
            cur = 0
            while stack and nums[stack[-1]] <= nums[i]:
                cur = max(cur, dp[stack.pop()])

            if stack:
                dp[i] = 1 + cur
            stack.append(i)

        return max(dp)