
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    result[i] += 1
                elif nums[i] < nums[j]:
                    result[j] += 1
        return result

