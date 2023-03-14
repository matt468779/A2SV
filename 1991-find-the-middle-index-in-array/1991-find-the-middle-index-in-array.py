class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        
        for i in range(len(nums)):
            rightSum -= nums[i]
            if rightSum == leftSum:
                return i
            leftSum += nums[i]
        
        return -1