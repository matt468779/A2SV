class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(lambda: 0)
        for num in arr:
            dp[num] = 1 + dp[num-difference]
        
        return max(dp.values())