class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k == 0:
            return
        def rotate_from_start(nums, start, k):
            nxt = (start+k) % len(nums)
            temp2 = nums[start]
            count = 1
            while nxt != start:
                temp = nums[nxt]
                nums[nxt] = temp2
                temp2 = temp
                nxt = (nxt+k)%len(nums)
                count += 1
            nums[nxt] = temp2
            return count
        
        count = 0
        i = 0
        while count < len(nums):
            count += rotate_from_start(nums, i, k)
            i += 1