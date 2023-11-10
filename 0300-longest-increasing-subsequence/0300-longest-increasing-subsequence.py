class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLength = [1] * len(nums)
        
        for i in range(1, len(nums)):
            soFar = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    soFar = max(soFar, maxLength[j])
            
            maxLength[i] += soFar
        
        return max(maxLength)