class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        last = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[last-1] or nums[last-1] != nums[last-2]:
                nums[last] = nums[i]
                last += 1
        
        return last
                