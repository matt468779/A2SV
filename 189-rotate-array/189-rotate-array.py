class Solution:
    def reverse(self, nums: List[int], begin: int, end:int) -> None:
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l =len(nums)
        if k%l == 0:
            return
        k = k % l
        right = True
        if k > len(nums)//2:
            right = False
            k = len(nums) - k
        
        begin = 0
        end = l-1
        for i in range(k):
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1
        if right:
            self.reverse(nums, 0, k-1)
            self.reverse(nums, k, l-k-1)
            self.reverse(nums, k, l-1)
        else:
            self.reverse(nums, k, l-k-1)
            self.reverse(nums, 0, l-k-1)
            self.reverse(nums, l-k, l-1)
            