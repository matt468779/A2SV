class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        cumulative = 0
        for num in derived:
            cumulative ^= num
        
        return not cumulative