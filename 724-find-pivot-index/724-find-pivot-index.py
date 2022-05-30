class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = [0]
        for i in range(len(nums)):
            rightSum.append(nums[i] + rightSum[i])
        l = len(nums)
        for i in range(len(nums)):
            if rightSum[i] == rightSum[l]-rightSum[i+1]:
                return i
        return -1