class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            right_sum -= nums[i]
            res[i] = abs(left_sum - right_sum)
            left_sum += nums[i]

        return res