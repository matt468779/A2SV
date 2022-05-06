class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        globalMax = 0
        for i in range(len(nums)):
            localMax = nums[i] + nums[len(nums)-i-1]
            if localMax > globalMax:
                globalMax = localMax

        return globalMax