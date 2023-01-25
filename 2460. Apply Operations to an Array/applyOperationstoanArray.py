class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        lastPointer = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastPointer] = nums[i]
                lastPointer += 1
            
            if lastPointer != i+1:
                nums[i] = 0
        
        return nums
