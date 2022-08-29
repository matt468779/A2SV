class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        s = []
        for i in range(l-1, -1, -1):
            while s and nums[i] >= s[-1]:
                s.pop()
            s.append(nums[i])
        
        res = [-1] * l
        for i in range(l-1, -1, -1):
            while s and nums[i] >= s[-1]:
                s.pop()
            s.append(nums[i])
            if len(s) > 1:
                res[i] = s[-2]
        
        return res