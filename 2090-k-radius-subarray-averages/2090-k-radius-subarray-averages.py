class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2*k + 1:
            return [-1] * len(nums
                             )
        res = [-1] * len(nums)
        pre_sum = sum(nums[:2*k+1])
        res[k] = pre_sum//(2*k+1)
        
        for i in range(k+1, len(nums)-k):
            pre_sum += nums[i+k] - nums[i-k-1]
            res[i] = pre_sum // (2*k+1)
        
        return res