class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        cumulative = 0
        for num in pref:
            res.append(cumulative ^ num)
            cumulative ^= res[-1]
        
        return res