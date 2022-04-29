class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        for num in nums :
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1

        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif i < zero+one:
                nums[i] = 1
            else:
                nums[i] = 2

