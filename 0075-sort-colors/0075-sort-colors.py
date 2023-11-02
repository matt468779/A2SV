class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0
        for num in nums:
            zeros += num == 0
            ones += num == 1
            twos += num == 2
        
        for i in range(zeros):
            nums[i] = 0
        for i in range(zeros, zeros+ones):
            nums[i] = 1
        for i in range(zeros+ones, len(nums)):
            nums[i] = 2