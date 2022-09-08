class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = [0] * (len(nums)+2)
        for i in range(len(nums)-1, -1, -1):
            robbed[i] = max(nums[i]+robbed[i+2], robbed[i+1])
            
        return robbed[0]
        
        