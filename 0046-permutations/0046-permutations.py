class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        self.state = 0
        def solve():
            if len(temp) == len(nums):
                res.append(list(temp))
                return 
            
            te = self.state
            for i in range(len(nums)):
                mask = 2**(len(nums)-i-1)
                if not mask & self.state:
                    temp.append(nums[i])
                    self.state |= mask
                    solve()
                    self.state = te
                    temp.pop()
            
        solve()
        return res