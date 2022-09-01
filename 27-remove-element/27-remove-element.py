class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        last = len(nums)-1
        while i <= last:
            if nums[i] == val and nums[last] != val:
                nums[i], nums[last] = nums[last], nums[i]
                i += 1
                last -= 1
            elif nums[i] != val:
                i += 1
            elif nums[last] == val:
                last -= 1
        return last+1
             