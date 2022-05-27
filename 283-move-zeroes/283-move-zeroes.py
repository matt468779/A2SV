class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstZero = 0
        while nums[firstZero] != 0 and firstZero < len(nums)-1:
            firstZero += 1

        for i in range(firstZero+1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[firstZero] = nums[firstZero], nums[i]
                firstZero += 1
                
            