class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            res.append('0' if nums[i][i] == '1' else '1')
        
        return ''.join(res)