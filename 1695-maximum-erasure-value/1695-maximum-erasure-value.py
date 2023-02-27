class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sub_set = set()
        l = 0
        res = 0
        sub_sum = 0
        for r in range(len(nums)):
            if nums[r] in sub_set:
                while nums[l] != nums[r]:
                    sub_set.remove(nums[l])
                    sub_sum -= nums[l]
                    l += 1
                l += 1
            else:
                sub_set.add(nums[r])
                sub_sum += nums[r]
                res = max(res, sub_sum)
                
        return res