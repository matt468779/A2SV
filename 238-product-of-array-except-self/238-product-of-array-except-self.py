class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1]
        after = [1]
        for i in range(len(nums)-1):
            before.append(before[i] * nums[i])

        for i in range(len(nums)-1, 0, -1):
            after.append(after[len(nums)-1-i] * nums[i])
            
        for i in range(len(nums)):
            before[i] = before[i]*after[len(nums)-i-1]
        return before