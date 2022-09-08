class Solution:
    def rob(self, nums: List[int]) -> int:
#         robbed = [0] * (len(nums)+2)
#         for i in range(len(nums)-1, -1, -1):
#             robbed[i] = max(nums[i]+robbed[i+2], robbed[i+1])
            
#         return robbed[0]
        
        robbed1, robbed2 = 0, 0
        for i in range(len(nums)-1, -1, -1):
            temp = robbed1
            robbed1 = max(nums[i]+robbed2, robbed1)
            robbed2 = temp
            
        return robbed1
            