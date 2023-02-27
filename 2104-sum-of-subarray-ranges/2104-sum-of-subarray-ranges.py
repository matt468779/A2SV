class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            sub_min = nums[i]
            sub_max = nums[i]
            for j in range(i+1, len(nums)):
                sub_min = min(sub_min, nums[j])
                sub_max = max(sub_max, nums[j])
                res += sub_max - sub_min
                
        return res