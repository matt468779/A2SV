class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(float('inf'))
        rang = [nums[0], nums[0]]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                rang[1] = nums[i]
            else:
                if rang[0] != rang[1]:
                    res.append(str(rang[0]) + '->' + str(rang[1]))
                else:
                    res.append(str(rang[0]))
                    
                rang = [nums[i], nums[i]]
        
        return res