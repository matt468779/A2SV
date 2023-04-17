class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        presum = [0] * (len(nums)+1)
        for i in range(1, len(presum)):
            presum[i] = presum[i-1] + nums[i-1]
            
        nextSmall = [len(nums)] * len(nums)
        prevSmall = [0] * len(nums)
        s = []
        for i in range(len(nums)-1, -1, -1):
            while s and nums[s[-1]] >= nums[i]:
                s.pop()
            if s:
                nextSmall[i] = s[-1]
            s.append(i)
            
        s = []
        for i in range(len(nums)):
            while s and nums[s[-1]] >= nums[i]:
                s.pop()
            
            if s:
                prevSmall[i] = s[-1] + 1
            s.append(i)

        res = 0
        for i in range(len(nums)):
            product = nums[i] * (presum[nextSmall[i]] - presum[prevSmall[i]])
            res = max(res, product)
        
        mod = 10**9 + 7
        return res % mod