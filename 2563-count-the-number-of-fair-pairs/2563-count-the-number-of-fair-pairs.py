class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()
        for i in range(1, len(nums)):
            right = bisect_right(nums, upper-nums[i], 0, i)
            left = bisect_left(nums, lower-nums[i], 0, i)

            res += right - left

                
        return res
