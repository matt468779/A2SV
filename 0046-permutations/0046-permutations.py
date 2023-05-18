class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def solve(state):
            if len(temp) == len(nums):
                res.append(list(temp))
                return 
            
            for i in range(len(nums)):
                mask = 2**(len(nums)-i-1)
                if not mask & state:
                    temp.append(nums[i])
                    solve(state | mask)
                    temp.pop()
            
        solve(0)
        return res