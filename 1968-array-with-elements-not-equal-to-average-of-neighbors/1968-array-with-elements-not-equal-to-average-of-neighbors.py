class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        length = len(nums)
        half = length//2
        nums.sort()
        if length % 2 == 1:
            half = length//2 + 1
            arr[length-1] = nums[length//2]
        else:
            half = length//2
        for i in range(0, length-1, 2):
            arr[i] = nums[i//2]
            arr[i+1] = nums[i//2+half]
        return arr