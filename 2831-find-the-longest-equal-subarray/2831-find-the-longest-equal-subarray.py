class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        def findMax(arr):
            res = 1
            l = 0
            r = 1
            while l <= r and r < len(arr):
                if arr[r] - arr[l] - (r - l) <= k:
                    res = max(res, r-l+1)
                    r += 1
                else:
                    l += 1
                    
            return res
                
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]].append(i)
            else:
                count[nums[i]] = [i]
        
        res = 1
        for num in count:
            res = max(res, findMax(count[num]))
        
        return res