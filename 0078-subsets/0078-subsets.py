class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def solve(ind):
            for i in range(ind, len(nums)):
                temp.append(nums[i])
                solve(i+1)
                temp.pop()
            res.append(temp.copy())
        
        solve(0)
        return res