class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        res = [0]
        def solve(i, nums_or):      
            if i >= len(nums):
                if nums_or == max_or:
                    res[0] += 1
                return
            
            solve(i+1, nums_or | nums[i])
            solve(i+1, nums_or)
        
        solve(0, 0)
        return res[0]