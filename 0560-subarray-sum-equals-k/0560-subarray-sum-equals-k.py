class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_dict = {0: 1}
        pre_sum = 0
        res = 0
        for num in nums:
            pre_sum += num
            res += pre_dict.get(pre_sum-k, 0)
            pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1
        
        return res
            