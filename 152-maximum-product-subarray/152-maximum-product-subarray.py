class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def multiply(nums):
            if not len(nums):
                return float('-inf')
            ans = 1
            for n in nums:
                ans *= n
            return ans
        
        dp = [nums[0]]
        res = nums[0]
        i = 0
        while i < len(nums):
            j = i
            neg = []
            even = True
            while j < len(nums) and nums[j] != 0:
                if nums[j] < 0:
                    even = not even
                    if len(neg) < 2:
                        neg.append(j)
                    else:
                        neg[-1] = j
                j += 1
            if not even:
                if len(neg) == 2:
                    res = max(res, multiply(nums[i:neg[-1]]), multiply(nums[neg[0]+1:j]))
                else:
                    res = max(res, multiply(nums[i:neg[0]]), nums[neg[0]], multiply(nums[neg[0]+1:j]))
            else:
                res = max(res, multiply(nums[i:j]))
            
            if j < len(nums):
                res = max(res, 0)
            i = j+1
            
        return res